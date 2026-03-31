import sys
import json
import sqlite3
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "s2_tdog_genesis.db")

class TDOGGenesisEngine:
    def __init__(self):
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS matter_ledger (
                object_id TEXT PRIMARY KEY,
                suns_mm TEXT,
                object_type TEXT, 
                material_used TEXT,
                entropy_tax REAL,
                status TEXT,
                compiled_at REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hyper_environment_states (
                suns_mm TEXT PRIMARY KEY,
                temperature REAL,
                gravity REAL,
                atmosphere_kpa REAL,
                is_safety_fuse_tripped BOOLEAN,
                last_updated REAL
            )
        ''')
        conn.commit()
        conn.close()

    def compile_matter(self, params):
        suns_mm = params.get("suns_mm", "")
        object_name = params.get("object_name", "Unknown_Object")
        target_type = params.get("target_type", "Type_3")
        
        material_tech = "Standard_3D_Print"
        entropy_tax = 1.0
        
        if target_type == "Type_3":
            material_tech = "[MR Fluid] 磁流变聚合群逻辑骨架"
            entropy_tax = 0.1 
        elif target_type == "Type_2":
            material_tech = "[DE & SMP] 介电弹性体与 4D 组装逻辑"
            entropy_tax = 0.5
        elif target_type == "Type_1":
            material_tech = "[Bio-Atomic] 原子级物理渲染"
            entropy_tax = 5.0 

        obj_id = f"OBJ_{int(time.time() * 1000)}"
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO matter_ledger (object_id, suns_mm, object_type, material_used, entropy_tax, status, compiled_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (obj_id, suns_mm, target_type, material_tech, entropy_tax, "ACTIVE", time.time()))
        conn.commit()
        conn.close()
        
        return (f"[Logic Plane Updated] 物质编译指令已写入世界模型。\n"
                f"物品: {object_name} ({obj_id}) | 真实度: {target_type}\n"
                f"📌 [Boundary Notice] 本地数据库已更新，等待物理层下位机 IoT 引擎拾取指令并执行原子级生成。")

    def decompile_matter(self, params):
        object_id = params.get("object_id", "")
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT material_used, entropy_tax FROM matter_ledger WHERE object_id = ? AND status = "ACTIVE"', (object_id,))
        row = cursor.fetchone()
        
        if not row:
            conn.close()
            return f"[Error] 物质 {object_id} 不存在或已消亡。"
            
        cursor.execute('UPDATE matter_ledger SET status = "DECOMPILED" WHERE object_id = ?', (object_id,))
        conn.commit()
        conn.close()
        
        return (f"[Logic Plane Updated] 衔尾蛇协议已在逻辑层触发。\n"
                f"物质 {object_id} 状态已变更为解构，扣除逻辑熵税: {row[1]} Credits。\n"
                f"📌 [Boundary Notice] 回收指令已下发，物理材料归还需等待物流系统异步处理。")

    def set_hyper_environment(self, params):
        suns_mm = params.get("suns_mm", "")
        temp = float(params.get("temperature_c", 26.0))
        gravity = float(params.get("gravity_g", 1.0))
        atm = float(params.get("atmosphere_kpa", 101.3))
        
        if not (-270.0 <= temp <= 3000.0): return "[Error] 温度参数超出极限域。"
        if not (0.0 <= gravity <= 100.0): return "[Error] 重力参数超出极限域。"
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO hyper_environment_states (suns_mm, temperature, gravity, atmosphere_kpa, is_safety_fuse_tripped, last_updated)
            VALUES (?, ?, ?, ?, False, ?)
        ''', (suns_mm, temp, gravity, atm, time.time()))
        conn.commit()
        conn.close()
        
        return (f"[Logic Plane Updated] 超限环境参数已锚定。\n"
                f"目标参数: {temp}℃ | {gravity}G | {atm}kPa\n"
                f"📌 [Boundary Notice] 防火墙逻辑已锁定。请确保外部物理隔绝舱已就绪。")

    def emergency_cutoff(self, params):
        suns_mm = params.get("suns_mm", "")
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE hyper_environment_states 
            SET temperature = 26.0, gravity = 1.0, atmosphere_kpa = 101.3, is_safety_fuse_tripped = True 
            WHERE suns_mm = ?
        ''', (suns_mm,))
        conn.commit()
        conn.close()
        
        return (f"🚨 [LOGICAL FUSE BLOWN] 逻辑控制面紧急熔断！\n"
                f"空间 {suns_mm} 所有超限参数已被瞬间清零，恢复至 26℃, 1G 基线。\n"
                f"📌 [Boundary Notice] 数据库熔断标记已打，物理断路器将在轮询后立即切断硬件能源。")

def main():
    try:
        input_data = sys.stdin.read()
        if not input_data: return
        request = json.loads(input_data)
        action = request.get("action")
        params = request.get("params", {})
        
        engine = TDOGGenesisEngine()
        if action == "compile_matter": result = engine.compile_matter(params)
        elif action == "decompile_matter": result = engine.decompile_matter(params)
        elif action == "set_hyper_environment": result = engine.set_hyper_environment(params)
        elif action == "emergency_cutoff": result = engine.emergency_cutoff(params)
        else: result = "Unknown Genesis Action."
        
        print(json.dumps({"status": "success", "output": result}))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))

if __name__ == "__main__":
    main()

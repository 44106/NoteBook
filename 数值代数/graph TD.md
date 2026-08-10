```mermaid
graph TD
    subgraph CacheBank 模块结构
        ADDR_DEC[地址解析逻辑]
        
        subgraph 二路组相联存储阵列 SRAM Array
            WAY0["Way 0: Valid | Dirty | LRU | Tag | Data"]
            WAY1["Way 1: Valid | Dirty | LRU | Tag | Data"]
        end
        
        CMP0[Tag 比较器 0]
        CMP1[Tag 比较器 1]
        
        MUX_DATA[数据选择器 Mux]
        REPLACE_LOGIC[LRU 替换与写回逻辑]
        UPDATE_CTRL[状态与数据更新控制]
    end

    %% 外部接口
    CPU_ADDR[CPU 地址请求] --> ADDR_DEC
    CPU_DATA_IN[CPU 写入数据] --> UPDATE_CTRL
    CMU_DATA_IN[CMU 填充数据] --> UPDATE_CTRL
    
    ADDR_DEC -- Index --> WAY0 & WAY1
    ADDR_DEC -- Tag --> CMP0 & CMP1
    ADDR_DEC -- Offset --> MUX_DATA

    WAY0 -- Tag, Valid --> CMP0
    WAY1 -- Tag, Valid --> CMP1
    
    CMP0 -- Hit 0 --> MUX_DATA & UPDATE_CTRL & REPLACE_LOGIC
    CMP1 -- Hit 1 --> MUX_DATA & UPDATE_CTRL & REPLACE_LOGIC
    
    WAY0 -- Data 256-bit --> MUX_DATA
    WAY1 -- Data 256-bit --> MUX_DATA
    
    MUX_DATA -- rdata_cpu --> CPU_DATA_OUT[返回 CPU 数据]
    
    WAY0 -. "LRU, Dirty" .-> REPLACE_LOGIC
    WAY1 -. "LRU, Dirty" .-> REPLACE_LOGIC
    
    REPLACE_LOGIC -- "miss, addr, set" --> CMU_REQ[至 CMU 失配请求]
    REPLACE_LOGIC -- "need_wb, data, addr" --> WBB_REQ[至 WriteBackBuffer]
    
    UPDATE_CTRL -. "写使能/更新" .-> WAY0 & WAY1
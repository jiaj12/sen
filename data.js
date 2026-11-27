window.TRAINING={version:'1.4.0',exercises:[
{id:'curl',name:'坐姿手臂弯举',equip:'轻水瓶250–500g；获专业允许且适应后才可试1kg',cue:'背靠椅背，上臂贴身，缓慢弯肘。',dose:'8次',seconds:40},
{id:'external',name:'坐姿肩外旋',equip:'空手或超轻弹力带',cue:'肘贴身体，前臂向外打开，不耸肩。',dose:'8次',seconds:40},
{id:'lateral_front',name:'坐姿低位侧抬',equip:'空手优先；适应后可用250g水瓶',cue:'双肘微屈，只抬到舒适的低位，不超过肩高。',dose:'8次',seconds:40},
{id:'knee',name:'坐姿单腿伸膝',equip:'自重，不绑沙袋',cue:'一次一条腿，膝盖只伸到不痛的范围，不锁膝。',dose:'左右各8次',seconds:90,unilateral:true},
{legacy:true,id:'slide',name:'仰卧脚跟滑动',equip:'床；不用下地',cue:'脚跟贴床滑动，不抬臀；上下床不便可跳过。',dose:'左右各8次',seconds:90,unilateral:true},
{defaultReps:12,min:6,max:15,id:'heel',name:'坐姿提踵',equip:'自重，不在膝上放重物',cue:'前脚掌贴地，缓慢抬脚跟。',dose:'12次',seconds:60},
{defaultReps:12,min:6,max:15,id:'toe',name:'坐姿抬脚尖',equip:'自重',cue:'脚跟贴地，慢慢抬起脚尖。',dose:'12次',seconds:60},
{id:'wrist',name:'支撑式腕屈伸',equip:'空手或轻水瓶',cue:'前臂放桌面，手腕轻柔活动；两侧分别练习。',dose:'左右各8次',seconds:90,unilateral:true},
{id:'row',candidate:true,name:'坐姿弹力带划船',equip:'超轻弹力带；可靠固定点',cue:'坐稳，肘向后拉，不前倾、不后仰；固定点可靠。',dose:'8次',seconds:40},
{id:'standcurl',candidate:true,defaultReps:6,min:4,max:10,name:'扶持站姿屈膝',equip:'固定台面；不负重',cue:'双手扶稳，单腿脚跟向后抬，身体直立；不适立即坐下。',dose:'左右各6次',seconds:70,unilateral:true},
{id:'standheel',candidate:true,defaultReps:12,min:6,max:15,name:'扶持站姿提踵',equip:'固定台面；不负重',cue:'双手扶稳，缓慢抬起脚跟；不适立即坐下。',dose:'12次',seconds:60}],plans:{A:{name:'A组 · 上肢为主',ids:['curl','knee','external','heel','lateral_front','toe']},B:{name:'B组 · 下肢为主',ids:['knee','lateral_front','external','toe','wrist','heel']},R:{name:'恢复日 · 舒缓活动',ids:[]}},expanded:{A:['curl','knee','row','heel','external','toe'],B:['lateral_front','knee','external','standcurl','wrist','standheel']}};

/****
192.168.1.153
�˺ţ� root
���룺123456
****/

select * from T_ReportBaseInfo

----  ��ѯ ӯ��Ԥ�⵼������
use vsatTemp
select a.REPORTCODE,b.Caption,
a.STOCKCODE,
a.PERIODDATE,,b.REPORTDATE as '����׫д����'
a.INDATE, a.TFPF0001,a.TFPF0020,a.TFPF0024,a.TFPF0016,a.msrepl_tran_version
from  T_FinancialPredict a ,T_ReportBaseInfo b
where a.indate>'2016-12-29 16:40' and a.REPORTCODE = b.code

---- ��ѯ Ŀ���
use vsatTemp
select b.CAPTION,a.* from T_StockPredict a,T_ReportBaseInfo b where a.indate>'2016-12-30' and a.REPORTCODE = b.code
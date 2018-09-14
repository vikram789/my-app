node ('VZW.POS.ODDBUILD.SERVER')  {
def retail_host = "10-119-0-74.ebiz.verizon.com"
def appprops_bcc_host = "10-119-10-80.ebiz.verizon.com"
def tele_b2b_care_host = "10-119-7-116.ebiz.verizon.com"
def vip_eai_gz_east_onprem_host = "obsneposzat17"
def vip_eai_gz_west_onprem_host = "twsneposzaq02"
def vip_eai_gz_east_aws_host = "10.119.9.83"
def vip_eai_gz_west_aws_host = "10.119.42.31"
def vip_eai_yz_east_onprem_host = "obsnesoyzaq01"
def vip_eai_yz_west_onprem_host ="twsnesoyzaq03"
def indirect_onprem_host = "twsneocyzat01"

def branches = [:]

println Channels 
def values = Channels.split(',')  
for(i=0;i<values.size();i++)
{
 switch(values[i]) {
	 case "B2B": 
	    branches["B2B"] = {	stage("B2B") { 
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${tele_b2b_care_host} /app/scripts/posenv/autodeploy/deploy_omni_new.sh atg-b2b ${Release_OMNI} poscomm1" 
			} }
		break
	 case "CARE": 
	    branches["CARE"] = {	stage("CARE") { 
		sh "sleep 45"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${tele_b2b_care_host} /app/scripts/posenv/autodeploy/deploy_omni_new.sh atg-care ${Release_OMNI} poscomm1" 
			} }
		break
	 case "TELE": 
	    branches["TELE"] = {	stage("TELE") { 
		sh "sleep 90"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${tele_b2b_care_host} /app/scripts/posenv/autodeploy/deploy_omni_new.sh atg-telesales ${Release_OMNI} poscomm1" 
			} }
		break
	 case "RETAIL": 
	    branches["RETAIL"] = {	stage("RETAIL") { 
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${retail_host} /app/scripts/posenv/autodeploy/deploy_omni_new.sh atg-retail ${Release_OMNI} poscomm1" 
			} }
		break
	 case "AppProperties": 
	    branches["AppProps"] = {	stage("AppProps") { 
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${appprops_bcc_host} /app/scripts/posenv/autodeploy/deploy_omni_new.sh atg-appproperties ${Release_OMNI} poscomm1" 
			} }
		break
	 case "Indirect": 
	    branches["Indirect"] = {	stage("Indirect") { 
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${indirect_onprem_host} /vzwhome/weblogic/AdminScripts/deploy_omni_new.sh atg-indirect uat1" 
			} }
		break
	 case "EAI-aws-east": 
	    branches["EAI-aws-east"] = {	stage("EAI-aws-east") { 
		sh "sleep 60"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_east_aws_host} /app/scripts/posenv/autodeploy/bin/autodeploy_eaisch.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "EAI-aws-west": 
	    branches["EAI-aws-west"] = {	stage("EAI-aws-west") { 
		sh "sleep 60"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_west_aws_host} /app/scripts/posenv/autodeploy/bin/autodeploy_eaisch.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "EAI-on-prem-east": 
	    branches["EAI-on-prem-east"] = {	stage("EAI-on-prem-east") { 
		sh "sleep 60"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_east_onprem_host} /app/scripts/autodeploy_eaisch.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "EAI-on-prem-west": 
	    branches["EAI-on-prem-west"] = {	stage("EAI-on-prem-west") { 
		sh "sleep 60"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_west_onprem_host} /app/scripts/autodeploy_eaisch.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "VIP-aws-east": 
	    branches["VIP-aws-east"] = {	stage("VIP-aws-east") { 
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_east_aws_host} /app/scripts/posenv/autodeploy/bin/autodeploy_vipsvcs.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "VIP-aws-west": 
	    branches["VIP-aws-west"] = {	stage("VIP-aws-west") { 
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_west_aws_host} /app/scripts/posenv/autodeploy/bin/autodeploy_vipsvcs.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "VIP-on-prem-east": 
	    branches["VIP-on-prem-east"] = {	stage("VIP-on-prem-east") { 
		// sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_east_onprem_host} /app/scripts/autodeploy_vipsvcs.sh ${Release_VIP_EAI}"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_east_onprem_host} /app/scripts/deploy_gz_vipsvc_active_inactive.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "VIP-on-prem-west": 
	    branches["VIP-on-prem-west"] = {	stage("VIP-on-prem-west") { 
		// sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_west_onprem_host} /app/scripts/autodeploy_vipsvcs.sh ${Release_VIP_EAI}"
		  sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_gz_west_onprem_host} /app/scripts/deploy_gz_vipsvc_active_inactive.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "VIP-East-YZ": 
	    branches["VIP-East-YZ"] = {	stage("VIP-East-YZ") { 
		sh "sleep 350"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_yz_east_onprem_host} /app/scripts/autodeploy_vipsvc-yz-active-inactive.sh" 
			} }
		break
	 case "VIP-West-YZ": 
	    branches["VIP-West-YZ"] = {	stage("VIP-West-YZ") { 
		sh "sleep 350"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_yz_west_onprem_host} /app/scripts/autodeploy_vipsvc-yz-active-inactive.sh" 
			} }
		break
	 case "EAI-East-YZ": 
	    branches["EAI-East-YZ"] = {	stage("EAI-East-YZ") { 
		sh "sleep 200"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_yz_east_onprem_host} /app/scripts/autodeploy_eai-yz.sh ${Release_VIP_EAI}" 
			} }
		break
	 case "EAI-West-YZ": 
	    branches["EAI-West-YZ"] = {	stage("EAI-West-YZ") { 
		sh "sleep 200"
		sh "/usr/bin/ssh -i /u01/posatgap/scmspace/weblogic_key -o StrictHostKeyChecking=no weblogic@${vip_eai_yz_west_onprem_host} /app/scripts/autodeploy_eai-yz.sh ${Release_VIP_EAI}" 
			} }
		break
	 default:
        println  "Invalid Arguments.. !!"	
		break
 }
}
parallel branches
}



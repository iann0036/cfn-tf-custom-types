# TF::ACI::OspfTimers

Manages ACI OSPF Timers

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::OspfTimers",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#bwref" title="BwRef">BwRef</a>" : <i>String</i>,
        "<a href="#ctrl" title="Ctrl">Ctrl</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dist" title="Dist">Dist</a>" : <i>String</i>,
        "<a href="#grctrl" title="GrCtrl">GrCtrl</a>" : <i>String</i>,
        "<a href="#lsaarrivalintvl" title="LsaArrivalIntvl">LsaArrivalIntvl</a>" : <i>String</i>,
        "<a href="#lsagppacingintvl" title="LsaGpPacingIntvl">LsaGpPacingIntvl</a>" : <i>String</i>,
        "<a href="#lsaholdintvl" title="LsaHoldIntvl">LsaHoldIntvl</a>" : <i>String</i>,
        "<a href="#lsamaxintvl" title="LsaMaxIntvl">LsaMaxIntvl</a>" : <i>String</i>,
        "<a href="#lsastartintvl" title="LsaStartIntvl">LsaStartIntvl</a>" : <i>String</i>,
        "<a href="#maxecmp" title="MaxEcmp">MaxEcmp</a>" : <i>String</i>,
        "<a href="#maxlsaaction" title="MaxLsaAction">MaxLsaAction</a>" : <i>String</i>,
        "<a href="#maxlsanum" title="MaxLsaNum">MaxLsaNum</a>" : <i>String</i>,
        "<a href="#maxlsaresetintvl" title="MaxLsaResetIntvl">MaxLsaResetIntvl</a>" : <i>String</i>,
        "<a href="#maxlsasleepcnt" title="MaxLsaSleepCnt">MaxLsaSleepCnt</a>" : <i>String</i>,
        "<a href="#maxlsasleepintvl" title="MaxLsaSleepIntvl">MaxLsaSleepIntvl</a>" : <i>String</i>,
        "<a href="#maxlsathresh" title="MaxLsaThresh">MaxLsaThresh</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#spfholdintvl" title="SpfHoldIntvl">SpfHoldIntvl</a>" : <i>String</i>,
        "<a href="#spfinitintvl" title="SpfInitIntvl">SpfInitIntvl</a>" : <i>String</i>,
        "<a href="#spfmaxintvl" title="SpfMaxIntvl">SpfMaxIntvl</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::OspfTimers
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#bwref" title="BwRef">BwRef</a>: <i>String</i>
    <a href="#ctrl" title="Ctrl">Ctrl</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dist" title="Dist">Dist</a>: <i>String</i>
    <a href="#grctrl" title="GrCtrl">GrCtrl</a>: <i>String</i>
    <a href="#lsaarrivalintvl" title="LsaArrivalIntvl">LsaArrivalIntvl</a>: <i>String</i>
    <a href="#lsagppacingintvl" title="LsaGpPacingIntvl">LsaGpPacingIntvl</a>: <i>String</i>
    <a href="#lsaholdintvl" title="LsaHoldIntvl">LsaHoldIntvl</a>: <i>String</i>
    <a href="#lsamaxintvl" title="LsaMaxIntvl">LsaMaxIntvl</a>: <i>String</i>
    <a href="#lsastartintvl" title="LsaStartIntvl">LsaStartIntvl</a>: <i>String</i>
    <a href="#maxecmp" title="MaxEcmp">MaxEcmp</a>: <i>String</i>
    <a href="#maxlsaaction" title="MaxLsaAction">MaxLsaAction</a>: <i>String</i>
    <a href="#maxlsanum" title="MaxLsaNum">MaxLsaNum</a>: <i>String</i>
    <a href="#maxlsaresetintvl" title="MaxLsaResetIntvl">MaxLsaResetIntvl</a>: <i>String</i>
    <a href="#maxlsasleepcnt" title="MaxLsaSleepCnt">MaxLsaSleepCnt</a>: <i>String</i>
    <a href="#maxlsasleepintvl" title="MaxLsaSleepIntvl">MaxLsaSleepIntvl</a>: <i>String</i>
    <a href="#maxlsathresh" title="MaxLsaThresh">MaxLsaThresh</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#spfholdintvl" title="SpfHoldIntvl">SpfHoldIntvl</a>: <i>String</i>
    <a href="#spfinitintvl" title="SpfInitIntvl">SpfInitIntvl</a>: <i>String</i>
    <a href="#spfmaxintvl" title="SpfMaxIntvl">SpfMaxIntvl</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for OSPF timers object.
- `description` - (Optional) Description for OSPF timers object.
- `bw_ref` - (Optional) OSPF policy bandwidth for OSPF timers object. Default value is "40000".
- `ctrl` - (Optional) Control state for OSPF timers object. It is in the form of comma separated string and allowed values are "name-lookup" and"pfx-suppress". To deselect both the options, just pass `ctrl=""`. Default value is "" that means none of the options are selected.
- `dist` - (Optional) Preferred administrative distance for OSPF timers object. Default value is "110".
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for OSPF timers object. Allowed value is "helper". Default value is "helper". To deselect the option, just pass `gr_ctrl=""`
- `lsa_arrival_intvl` - (Optional) Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRef

OSPF policy bandwidth for OSPF timers object. Default value is "40000".
- `ctrl` - (Optional) Control state for OSPF timers object. It is in the form of comma separated string and allowed values are "name-lookup" and"pfx-suppress". To deselect both the options, just pass `ctrl=""`. Default value is "" that means none of the options are selected.
- `dist` - (Optional) Preferred administrative distance for OSPF timers object. Default value is "110".
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for OSPF timers object. Allowed value is "helper". Default value is "helper". To deselect the option, just pass `gr_ctrl=""`
- `lsa_arrival_intvl` - (Optional) Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ctrl

Control state for OSPF timers object. It is in the form of comma separated string and allowed values are "name-lookup" and"pfx-suppress". To deselect both the options, just pass `ctrl=""`. Default value is "" that means none of the options are selected.
- `dist` - (Optional) Preferred administrative distance for OSPF timers object. Default value is "110".
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for OSPF timers object. Allowed value is "helper". Default value is "helper". To deselect the option, just pass `gr_ctrl=""`
- `lsa_arrival_intvl` - (Optional) Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for OSPF timers object.
- `bw_ref` - (Optional) OSPF policy bandwidth for OSPF timers object. Default value is "40000".
- `ctrl` - (Optional) Control state for OSPF timers object. It is in the form of comma separated string and allowed values are "name-lookup" and"pfx-suppress". To deselect both the options, just pass `ctrl=""`. Default value is "" that means none of the options are selected.
- `dist` - (Optional) Preferred administrative distance for OSPF timers object. Default value is "110".
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for OSPF timers object. Allowed value is "helper". Default value is "helper". To deselect the option, just pass `gr_ctrl=""`
- `lsa_arrival_intvl` - (Optional) Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dist

Preferred administrative distance for OSPF timers object. Default value is "110".
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for OSPF timers object. Allowed value is "helper". Default value is "helper". To deselect the option, just pass `gr_ctrl=""`
- `lsa_arrival_intvl` - (Optional) Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrCtrl

Graceful restart enabled or helper only for OSPF timers object. Allowed value is "helper". Default value is "helper". To deselect the option, just pass `gr_ctrl=""`
- `lsa_arrival_intvl` - (Optional) Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LsaArrivalIntvl

Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LsaGpPacingIntvl

LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LsaHoldIntvl

Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LsaMaxIntvl

throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LsaStartIntvl

Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxEcmp

Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLsaAction

Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLsaNum

Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLsaResetIntvl

Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLsaSleepCnt

Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLsaSleepIntvl

Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLsaThresh

Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of OSPF timers object.
- `annotation` - (Optional) Annotation for OSPF timers object.
- `description` - (Optional) Description for OSPF timers object.
- `bw_ref` - (Optional) OSPF policy bandwidth for OSPF timers object. Default value is "40000".
- `ctrl` - (Optional) Control state for OSPF timers object. It is in the form of comma separated string and allowed values are "name-lookup" and"pfx-suppress". To deselect both the options, just pass `ctrl=""`. Default value is "" that means none of the options are selected.
- `dist` - (Optional) Preferred administrative distance for OSPF timers object. Default value is "110".
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for OSPF timers object. Allowed value is "helper". Default value is "helper". To deselect the option, just pass `gr_ctrl=""`
- `lsa_arrival_intvl` - (Optional) Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpfHoldIntvl

Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpfInitIntvl

Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpfMaxIntvl

Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent tenant object.
- `name` - (Required) Name of OSPF timers object.
- `annotation` - (Optional) Annotation for OSPF timers object.
- `description` - (Optional) Description for OSPF timers object.
- `bw_ref` - (Optional) OSPF policy bandwidth for OSPF timers object. Default value is "40000".
- `ctrl` - (Optional) Control state for OSPF timers object. It is in the form of comma separated string and allowed values are "name-lookup" and"pfx-suppress". To deselect both the options, just pass `ctrl=""`. Default value is "" that means none of the options are selected.
- `dist` - (Optional) Preferred administrative distance for OSPF timers object. Default value is "110".
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for OSPF timers object. Allowed value is "helper". Default value is "helper". To deselect the option, just pass `gr_ctrl=""`
- `lsa_arrival_intvl` - (Optional) Minimum interval between the arrivals of lsas for OSPF timers object. Default value is "1000".
- `lsa_gp_pacing_intvl` - (Optional) LSA group pacing interval for OSPF timers object. Default value is "10".
- `lsa_hold_intvl` - (Optional) Throttle hold interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_max_intvl` - (Optional) throttle max interval between LSAs for OSPF timers object. Default value is "5000".
- `lsa_start_intvl` - (Optional) Throttle start-wait interval between LSAs for OSPF timers object. Default value is "0".
- `max_ecmp` - (Optional) Maximum ECMP for OSPF timers object. Default value is "8".
- `max_lsa_action` - (Optional) Action to take when maximum LSA limit is reached for OSPF timers object. Allowed values are "reject", "log" and "restart". Default value is "reject".
- `max_lsa_num` - (Optional) Maximum number of LSAs that are not self-generated for OSPF timers object. Default value is "20000".
- `max_lsa_reset_intvl` - (Optional) Time until the sleep count is reset to zero for OSPF timers object. Default value is "10".
- `max_lsa_sleep_cnt` - (Optional) Number of times OSPF can be placed in sleep state for OSPF timers object. Default value is "5".
- `max_lsa_sleep_intvl` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "5".
- `max_lsa_thresh` - (Optional) Maximum LSA threshold for OSPF timers object. Default value is "75".
- `name_alias` - (Optional) Name alias for OSPF timers object.
- `spf_hold_intvl` - (Optional) Minimum hold time between SPF calculations for OSPF timers object. Default value is "1000".
- `spf_init_intvl` - (Optional) Initial delay interval for the spf schedule for OSPF timers object. Default value is "200".
- `spf_max_intvl` - (Optional) Maximum interval between SPF calculations for OSPF timers object. Default value is "5000".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


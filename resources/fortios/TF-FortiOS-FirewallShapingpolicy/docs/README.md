# TF::FortiOS::FirewallShapingpolicy

Configure shaping policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallShapingpolicy",
    "Properties" : {
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>Double</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#diffservforward" title="DiffservForward">DiffservForward</a>" : <i>String</i>,
        "<a href="#diffservreverse" title="DiffservReverse">DiffservReverse</a>" : <i>String</i>,
        "<a href="#diffservcodeforward" title="DiffservcodeForward">DiffservcodeForward</a>" : <i>String</i>,
        "<a href="#diffservcoderev" title="DiffservcodeRev">DiffservcodeRev</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
        "<a href="#internetservice" title="InternetService">InternetService</a>" : <i>String</i>,
        "<a href="#internetservicesrc" title="InternetServiceSrc">InternetServiceSrc</a>" : <i>String</i>,
        "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#peripshaper" title="PerIpShaper">PerIpShaper</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tos" title="Tos">Tos</a>" : <i>String</i>,
        "<a href="#tosmask" title="TosMask">TosMask</a>" : <i>String</i>,
        "<a href="#tosnegate" title="TosNegate">TosNegate</a>" : <i>String</i>,
        "<a href="#trafficshaper" title="TrafficShaper">TrafficShaper</a>" : <i>String</i>,
        "<a href="#trafficshaperreverse" title="TrafficShaperReverse">TrafficShaperReverse</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#appcategory" title="AppCategory">AppCategory</a>" : <i>[ <a href="appcategorydefinition.md">AppCategoryDefinition</a>, ... ]</i>,
        "<a href="#appgroup" title="AppGroup">AppGroup</a>" : <i>[ <a href="appgroupdefinition.md">AppGroupDefinition</a>, ... ]</i>,
        "<a href="#application" title="Application">Application</a>" : <i>[ <a href="applicationdefinition.md">ApplicationDefinition</a>, ... ]</i>,
        "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ <a href="dstaddrdefinition.md">DstaddrDefinition</a>, ... ]</i>,
        "<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>" : <i>[ <a href="dstaddr6definition.md">Dstaddr6Definition</a>, ... ]</i>,
        "<a href="#dstintf" title="Dstintf">Dstintf</a>" : <i>[ <a href="dstintfdefinition.md">DstintfDefinition</a>, ... ]</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ <a href="groupsdefinition.md">GroupsDefinition</a>, ... ]</i>,
        "<a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>" : <i>[ <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>, ... ]</i>,
        "<a href="#internetservicecustomgroup" title="InternetServiceCustomGroup">InternetServiceCustomGroup</a>" : <i>[ <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicegroup" title="InternetServiceGroup">InternetServiceGroup</a>" : <i>[ <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a>, ... ]</i>,
        "<a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>" : <i>[ <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>, ... ]</i>,
        "<a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>" : <i>[ <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrccustom" title="InternetServiceSrcCustom">InternetServiceSrcCustom</a>" : <i>[ <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrccustomgroup" title="InternetServiceSrcCustomGroup">InternetServiceSrcCustomGroup</a>" : <i>[ <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcgroup" title="InternetServiceSrcGroup">InternetServiceSrcGroup</a>" : <i>[ <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcid" title="InternetServiceSrcId">InternetServiceSrcId</a>" : <i>[ <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcname" title="InternetServiceSrcName">InternetServiceSrcName</a>" : <i>[ <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a>, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>,
        "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>[ <a href="srcaddrdefinition.md">SrcaddrDefinition</a>, ... ]</i>,
        "<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>" : <i>[ <a href="srcaddr6definition.md">Srcaddr6Definition</a>, ... ]</i>,
        "<a href="#srcintf" title="Srcintf">Srcintf</a>" : <i>[ <a href="srcintfdefinition.md">SrcintfDefinition</a>, ... ]</i>,
        "<a href="#urlcategory" title="UrlCategory">UrlCategory</a>" : <i>[ <a href="urlcategorydefinition.md">UrlCategoryDefinition</a>, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallShapingpolicy
Properties:
    <a href="#classid" title="ClassId">ClassId</a>: <i>Double</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#diffservforward" title="DiffservForward">DiffservForward</a>: <i>String</i>
    <a href="#diffservreverse" title="DiffservReverse">DiffservReverse</a>: <i>String</i>
    <a href="#diffservcodeforward" title="DiffservcodeForward">DiffservcodeForward</a>: <i>String</i>
    <a href="#diffservcoderev" title="DiffservcodeRev">DiffservcodeRev</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
    <a href="#internetservice" title="InternetService">InternetService</a>: <i>String</i>
    <a href="#internetservicesrc" title="InternetServiceSrc">InternetServiceSrc</a>: <i>String</i>
    <a href="#ipversion" title="IpVersion">IpVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#peripshaper" title="PerIpShaper">PerIpShaper</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tos" title="Tos">Tos</a>: <i>String</i>
    <a href="#tosmask" title="TosMask">TosMask</a>: <i>String</i>
    <a href="#tosnegate" title="TosNegate">TosNegate</a>: <i>String</i>
    <a href="#trafficshaper" title="TrafficShaper">TrafficShaper</a>: <i>String</i>
    <a href="#trafficshaperreverse" title="TrafficShaperReverse">TrafficShaperReverse</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#appcategory" title="AppCategory">AppCategory</a>: <i>
      - <a href="appcategorydefinition.md">AppCategoryDefinition</a></i>
    <a href="#appgroup" title="AppGroup">AppGroup</a>: <i>
      - <a href="appgroupdefinition.md">AppGroupDefinition</a></i>
    <a href="#application" title="Application">Application</a>: <i>
      - <a href="applicationdefinition.md">ApplicationDefinition</a></i>
    <a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - <a href="dstaddrdefinition.md">DstaddrDefinition</a></i>
    <a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>: <i>
      - <a href="dstaddr6definition.md">Dstaddr6Definition</a></i>
    <a href="#dstintf" title="Dstintf">Dstintf</a>: <i>
      - <a href="dstintfdefinition.md">DstintfDefinition</a></i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - <a href="groupsdefinition.md">GroupsDefinition</a></i>
    <a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>: <i>
      - <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a></i>
    <a href="#internetservicecustomgroup" title="InternetServiceCustomGroup">InternetServiceCustomGroup</a>: <i>
      - <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a></i>
    <a href="#internetservicegroup" title="InternetServiceGroup">InternetServiceGroup</a>: <i>
      - <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a></i>
    <a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>: <i>
      - <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a></i>
    <a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>: <i>
      - <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a></i>
    <a href="#internetservicesrccustom" title="InternetServiceSrcCustom">InternetServiceSrcCustom</a>: <i>
      - <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a></i>
    <a href="#internetservicesrccustomgroup" title="InternetServiceSrcCustomGroup">InternetServiceSrcCustomGroup</a>: <i>
      - <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a></i>
    <a href="#internetservicesrcgroup" title="InternetServiceSrcGroup">InternetServiceSrcGroup</a>: <i>
      - <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a></i>
    <a href="#internetservicesrcid" title="InternetServiceSrcId">InternetServiceSrcId</a>: <i>
      - <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a></i>
    <a href="#internetservicesrcname" title="InternetServiceSrcName">InternetServiceSrcName</a>: <i>
      - <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a></i>
    <a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
    <a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>
      - <a href="srcaddrdefinition.md">SrcaddrDefinition</a></i>
    <a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>: <i>
      - <a href="srcaddr6definition.md">Srcaddr6Definition</a></i>
    <a href="#srcintf" title="Srcintf">Srcintf</a>: <i>
      - <a href="srcintfdefinition.md">SrcintfDefinition</a></i>
    <a href="#urlcategory" title="UrlCategory">UrlCategory</a>: <i>
      - <a href="urlcategorydefinition.md">UrlCategoryDefinition</a></i>
    <a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### ClassId

Traffic class ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservForward

Enable to change packet's DiffServ values to the specified diffservcode-forward value. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservReverse

Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservcodeForward

Change packet's DiffServ to this value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservcodeRev

Change packet's reverse (reply) DiffServ to this value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

Shaping policy ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetService

Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.  Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrc

Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.  Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

Apply this traffic shaping policy to IPv4 or IPv6 traffic. Valid values: `4`, `6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Shaping policy name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerIpShaper

Per-IP traffic shaper to apply with this policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

Schedule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this traffic shaping policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tos

ToS (Type of Service) value used for comparison.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TosMask

Non-zero bit positions are used for comparison while zero bit positions are ignored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TosNegate

Enable negated TOS match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficShaper

Traffic shaper to apply to traffic forwarded by the firewall policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficShaperReverse

Traffic shaper to apply to response traffic received by the firewall policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppCategory

_Required_: No

_Type_: List of <a href="appcategorydefinition.md">AppCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppGroup

_Required_: No

_Type_: List of <a href="appgroupdefinition.md">AppGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

_Required_: No

_Type_: List of <a href="applicationdefinition.md">ApplicationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

_Required_: No

_Type_: List of <a href="dstaddrdefinition.md">DstaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr6

_Required_: No

_Type_: List of <a href="dstaddr6definition.md">Dstaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstintf

_Required_: No

_Type_: List of <a href="dstintfdefinition.md">DstintfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of <a href="groupsdefinition.md">GroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustom

_Required_: No

_Type_: List of <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustomGroup

_Required_: No

_Type_: List of <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceGroup

_Required_: No

_Type_: List of <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceId

_Required_: No

_Type_: List of <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceName

_Required_: No

_Type_: List of <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcCustom

_Required_: No

_Type_: List of <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcCustomGroup

_Required_: No

_Type_: List of <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcGroup

_Required_: No

_Type_: List of <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcId

_Required_: No

_Type_: List of <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcName

_Required_: No

_Type_: List of <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

_Required_: No

_Type_: List of <a href="srcaddrdefinition.md">SrcaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr6

_Required_: No

_Type_: List of <a href="srcaddr6definition.md">Srcaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcintf

_Required_: No

_Type_: List of <a href="srcintfdefinition.md">SrcintfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlCategory

_Required_: No

_Type_: List of <a href="urlcategorydefinition.md">UrlCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

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


# TF::Thunder::SlbTemplatePolicy LidListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actionvalue" title="ActionValue">ActionValue</a>" : <i>String</i>,
    "<a href="#bwper" title="BwPer">BwPer</a>" : <i>Double</i>,
    "<a href="#bwratelimit" title="BwRateLimit">BwRateLimit</a>" : <i>Double</i>,
    "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
    "<a href="#connper" title="ConnPer">ConnPer</a>" : <i>Double</i>,
    "<a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>" : <i>Double</i>,
    "<a href="#directaction" title="DirectAction">DirectAction</a>" : <i>Double</i>,
    "<a href="#directactioninterval" title="DirectActionInterval">DirectActionInterval</a>" : <i>Double</i>,
    "<a href="#directactionvalue" title="DirectActionValue">DirectActionValue</a>" : <i>String</i>,
    "<a href="#directfail" title="DirectFail">DirectFail</a>" : <i>Double</i>,
    "<a href="#directloggingdrprst" title="DirectLoggingDrpRst">DirectLoggingDrpRst</a>" : <i>Double</i>,
    "<a href="#directpbslbinterval" title="DirectPbslbInterval">DirectPbslbInterval</a>" : <i>Double</i>,
    "<a href="#directpbslblogging" title="DirectPbslbLogging">DirectPbslbLogging</a>" : <i>Double</i>,
    "<a href="#directservicegroup" title="DirectServiceGroup">DirectServiceGroup</a>" : <i>String</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
    "<a href="#lidnum" title="Lidnum">Lidnum</a>" : <i>Double</i>,
    "<a href="#lockout" title="Lockout">Lockout</a>" : <i>Double</i>,
    "<a href="#log" title="Log">Log</a>" : <i>Double</i>,
    "<a href="#overlimitaction" title="OverLimitAction">OverLimitAction</a>" : <i>Double</i>,
    "<a href="#requestlimit" title="RequestLimit">RequestLimit</a>" : <i>Double</i>,
    "<a href="#requestper" title="RequestPer">RequestPer</a>" : <i>Double</i>,
    "<a href="#requestratelimit" title="RequestRateLimit">RequestRateLimit</a>" : <i>Double</i>,
    "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#dns64" title="Dns64">Dns64</a>" : <i>[ <a href="dns64definition.md">Dns64Definition</a>, ... ]</i>,
    "<a href="#responsecoderatelimit" title="ResponseCodeRateLimit">ResponseCodeRateLimit</a>" : <i>[ <a href="responsecoderatelimitdefinition.md">ResponseCodeRateLimitDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actionvalue" title="ActionValue">ActionValue</a>: <i>String</i>
<a href="#bwper" title="BwPer">BwPer</a>: <i>Double</i>
<a href="#bwratelimit" title="BwRateLimit">BwRateLimit</a>: <i>Double</i>
<a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
<a href="#connper" title="ConnPer">ConnPer</a>: <i>Double</i>
<a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>: <i>Double</i>
<a href="#directaction" title="DirectAction">DirectAction</a>: <i>Double</i>
<a href="#directactioninterval" title="DirectActionInterval">DirectActionInterval</a>: <i>Double</i>
<a href="#directactionvalue" title="DirectActionValue">DirectActionValue</a>: <i>String</i>
<a href="#directfail" title="DirectFail">DirectFail</a>: <i>Double</i>
<a href="#directloggingdrprst" title="DirectLoggingDrpRst">DirectLoggingDrpRst</a>: <i>Double</i>
<a href="#directpbslbinterval" title="DirectPbslbInterval">DirectPbslbInterval</a>: <i>Double</i>
<a href="#directpbslblogging" title="DirectPbslbLogging">DirectPbslbLogging</a>: <i>Double</i>
<a href="#directservicegroup" title="DirectServiceGroup">DirectServiceGroup</a>: <i>String</i>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
<a href="#lidnum" title="Lidnum">Lidnum</a>: <i>Double</i>
<a href="#lockout" title="Lockout">Lockout</a>: <i>Double</i>
<a href="#log" title="Log">Log</a>: <i>Double</i>
<a href="#overlimitaction" title="OverLimitAction">OverLimitAction</a>: <i>Double</i>
<a href="#requestlimit" title="RequestLimit">RequestLimit</a>: <i>Double</i>
<a href="#requestper" title="RequestPer">RequestPer</a>: <i>Double</i>
<a href="#requestratelimit" title="RequestRateLimit">RequestRateLimit</a>: <i>Double</i>
<a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#dns64" title="Dns64">Dns64</a>: <i>
      - <a href="dns64definition.md">Dns64Definition</a></i>
<a href="#responsecoderatelimit" title="ResponseCodeRateLimit">ResponseCodeRateLimit</a>: <i>
      - <a href="responsecoderatelimitdefinition.md">ResponseCodeRateLimitDefinition</a></i>
</pre>

## Properties

#### ActionValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwPer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnPer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRateLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectAction

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectActionInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectActionValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectLoggingDrpRst

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectPbslbInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectPbslbLogging

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectServiceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lidnum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lockout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverLimitAction

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestRateLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns64

_Required_: No

_Type_: List of <a href="dns64definition.md">Dns64Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCodeRateLimit

_Required_: No

_Type_: List of <a href="responsecoderatelimitdefinition.md">ResponseCodeRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


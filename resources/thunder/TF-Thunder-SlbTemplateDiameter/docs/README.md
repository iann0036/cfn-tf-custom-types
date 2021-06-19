# TF::Thunder::SlbTemplateDiameter

`thunder_slb_template_diameter` Provides details about thunder slb template diameter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateDiameter",
    "Properties" : {
        "<a href="#avpcode" title="AvpCode">AvpCode</a>" : <i>Double</i>,
        "<a href="#avpstring" title="AvpString">AvpString</a>" : <i>String</i>,
        "<a href="#customizecea" title="CustomizeCea">CustomizeCea</a>" : <i>Double</i>,
        "<a href="#dwrtime" title="DwrTime">DwrTime</a>" : <i>Double</i>,
        "<a href="#dwrupretry" title="DwrUpRetry">DwrUpRetry</a>" : <i>Double</i>,
        "<a href="#forwardtolatestserver" title="ForwardToLatestServer">ForwardToLatestServer</a>" : <i>Double</i>,
        "<a href="#forwardunknownsessionid" title="ForwardUnknownSessionId">ForwardUnknownSessionId</a>" : <i>Double</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#loadbalanceonsessionid" title="LoadBalanceOnSessionId">LoadBalanceOnSessionId</a>" : <i>Double</i>,
        "<a href="#multipleoriginhost" title="MultipleOriginHost">MultipleOriginHost</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#originrealm" title="OriginRealm">OriginRealm</a>" : <i>String</i>,
        "<a href="#productname" title="ProductName">ProductName</a>" : <i>String</i>,
        "<a href="#servicegroupname" title="ServiceGroupName">ServiceGroupName</a>" : <i>String</i>,
        "<a href="#sessionage" title="SessionAge">SessionAge</a>" : <i>Double</i>,
        "<a href="#terminateonccat" title="TerminateOnCcaT">TerminateOnCcaT</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vendorid" title="VendorId">VendorId</a>" : <i>Double</i>,
        "<a href="#avplist" title="AvpList">AvpList</a>" : <i>[ <a href="avplistdefinition.md">AvpListDefinition</a>, ... ]</i>,
        "<a href="#messagecodelist" title="MessageCodeList">MessageCodeList</a>" : <i>[ <a href="messagecodelistdefinition.md">MessageCodeListDefinition</a>, ... ]</i>,
        "<a href="#originhost" title="OriginHost">OriginHost</a>" : <i>[ <a href="originhostdefinition.md">OriginHostDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateDiameter
Properties:
    <a href="#avpcode" title="AvpCode">AvpCode</a>: <i>Double</i>
    <a href="#avpstring" title="AvpString">AvpString</a>: <i>String</i>
    <a href="#customizecea" title="CustomizeCea">CustomizeCea</a>: <i>Double</i>
    <a href="#dwrtime" title="DwrTime">DwrTime</a>: <i>Double</i>
    <a href="#dwrupretry" title="DwrUpRetry">DwrUpRetry</a>: <i>Double</i>
    <a href="#forwardtolatestserver" title="ForwardToLatestServer">ForwardToLatestServer</a>: <i>Double</i>
    <a href="#forwardunknownsessionid" title="ForwardUnknownSessionId">ForwardUnknownSessionId</a>: <i>Double</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#loadbalanceonsessionid" title="LoadBalanceOnSessionId">LoadBalanceOnSessionId</a>: <i>Double</i>
    <a href="#multipleoriginhost" title="MultipleOriginHost">MultipleOriginHost</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#originrealm" title="OriginRealm">OriginRealm</a>: <i>String</i>
    <a href="#productname" title="ProductName">ProductName</a>: <i>String</i>
    <a href="#servicegroupname" title="ServiceGroupName">ServiceGroupName</a>: <i>String</i>
    <a href="#sessionage" title="SessionAge">SessionAge</a>: <i>Double</i>
    <a href="#terminateonccat" title="TerminateOnCcaT">TerminateOnCcaT</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vendorid" title="VendorId">VendorId</a>: <i>Double</i>
    <a href="#avplist" title="AvpList">AvpList</a>: <i>
      - <a href="avplistdefinition.md">AvpListDefinition</a></i>
    <a href="#messagecodelist" title="MessageCodeList">MessageCodeList</a>: <i>
      - <a href="messagecodelistdefinition.md">MessageCodeListDefinition</a></i>
    <a href="#originhost" title="OriginHost">OriginHost</a>: <i>
      - <a href="originhostdefinition.md">OriginHostDefinition</a></i>
</pre>

## Properties

#### AvpCode

avp code.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvpString

pattern to be matched in the avp string name, max length 127 bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizeCea

customizing cea response.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DwrTime

dwr health-check timer interval (in 100 milli second unit, default is 100, 0 means unset this option).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DwrUpRetry

number of successful dwr health-check before declaring target up.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardToLatestServer

Forward client message to the latest server that sends message with the same session id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardUnknownSessionId

Forward server message even it has unknown session id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

user sesison idle timeout (in minutes, default is 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalanceOnSessionId

Load balance based on the session id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultipleOriginHost

allowing multiple origin-host to a single server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

diameter template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginRealm

origin-realm name avp.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductName

product name avp.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupName

service group name, this is the service group that the message needs to be copied to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAge

user session age allowed (default 10), this is not idle-time (in minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateOnCcaT

remove diameter session when receiving CCA-T message.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VendorId

vendor-id avp (Vendon Id).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvpList

_Required_: No

_Type_: List of <a href="avplistdefinition.md">AvpListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageCodeList

_Required_: No

_Type_: List of <a href="messagecodelistdefinition.md">MessageCodeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginHost

_Required_: No

_Type_: List of <a href="originhostdefinition.md">OriginHostDefinition</a>

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


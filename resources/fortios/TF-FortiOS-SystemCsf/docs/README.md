# TF::FortiOS::SystemCsf

Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemCsf",
    "Properties" : {
        "<a href="#acceptauthbycert" title="AcceptAuthByCert">AcceptAuthByCert</a>" : <i>String</i>,
        "<a href="#authorizationrequesttype" title="AuthorizationRequestType">AuthorizationRequestType</a>" : <i>String</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#configurationsync" title="ConfigurationSync">ConfigurationSync</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#fabricobjectunification" title="FabricObjectUnification">FabricObjectUnification</a>" : <i>String</i>,
        "<a href="#fixedkey" title="FixedKey">FixedKey</a>" : <i>String</i>,
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#grouppassword" title="GroupPassword">GroupPassword</a>" : <i>String</i>,
        "<a href="#managementip" title="ManagementIp">ManagementIp</a>" : <i>String</i>,
        "<a href="#managementport" title="ManagementPort">ManagementPort</a>" : <i>Double</i>,
        "<a href="#samlconfigurationsync" title="SamlConfigurationSync">SamlConfigurationSync</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#upstreamip" title="UpstreamIp">UpstreamIp</a>" : <i>String</i>,
        "<a href="#upstreamport" title="UpstreamPort">UpstreamPort</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#fabricdevice" title="FabricDevice">FabricDevice</a>" : <i>[ <a href="fabricdevicedefinition.md">FabricDeviceDefinition</a>, ... ]</i>,
        "<a href="#trustedlist" title="TrustedList">TrustedList</a>" : <i>[ <a href="trustedlistdefinition.md">TrustedListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemCsf
Properties:
    <a href="#acceptauthbycert" title="AcceptAuthByCert">AcceptAuthByCert</a>: <i>String</i>
    <a href="#authorizationrequesttype" title="AuthorizationRequestType">AuthorizationRequestType</a>: <i>String</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#configurationsync" title="ConfigurationSync">ConfigurationSync</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#fabricobjectunification" title="FabricObjectUnification">FabricObjectUnification</a>: <i>String</i>
    <a href="#fixedkey" title="FixedKey">FixedKey</a>: <i>String</i>
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#grouppassword" title="GroupPassword">GroupPassword</a>: <i>String</i>
    <a href="#managementip" title="ManagementIp">ManagementIp</a>: <i>String</i>
    <a href="#managementport" title="ManagementPort">ManagementPort</a>: <i>Double</i>
    <a href="#samlconfigurationsync" title="SamlConfigurationSync">SamlConfigurationSync</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#upstreamip" title="UpstreamIp">UpstreamIp</a>: <i>String</i>
    <a href="#upstreamport" title="UpstreamPort">UpstreamPort</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#fabricdevice" title="FabricDevice">FabricDevice</a>: <i>
      - <a href="fabricdevicedefinition.md">FabricDeviceDefinition</a></i>
    <a href="#trustedlist" title="TrustedList">TrustedList</a>: <i>
      - <a href="trustedlistdefinition.md">TrustedListDefinition</a></i>
</pre>

## Properties

#### AcceptAuthByCert

Accept connections with unknown certificates and ask admin for approval. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationRequestType

Authorization request type. Valid values: `serial`, `certificate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

Certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationSync

Configuration sync mode. Valid values: `default`, `local`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricObjectUnification

Fabric CMDB Object Unification Valid values: `default`, `local`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedKey

Auto-generated fixed key used when this device is the root. (Will automatically be generated if not set.).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

Security Fabric group name. All FortiGates in a Security Fabric must have the same group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupPassword

Security Fabric group password. All FortiGates in a Security Fabric must have the same group password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementIp

Management IP address of this FortiGate. Used to log into this FortiGate from another FortiGate in the Security Fabric.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementPort

Overriding port for management connection (Overrides admin port).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamlConfigurationSync

SAML setting configuration synchronization. Valid values: `default`, `local`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable Security Fabric. Valid values: `enable`, `disable`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamIp

IP address of the FortiGate upstream from this FortiGate in the Security Fabric.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamPort

The port number to use to communicate with the FortiGate upstream from this FortiGate in the Security Fabric (default = 8013).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricDevice

_Required_: No

_Type_: List of <a href="fabricdevicedefinition.md">FabricDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedList

_Required_: No

_Type_: List of <a href="trustedlistdefinition.md">TrustedListDefinition</a>

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


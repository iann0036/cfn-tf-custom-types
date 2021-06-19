# TF::Thunder::Glm

`thunder_glm` Provides details about thunder glm

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::Glm",
    "Properties" : {
        "<a href="#allocatebandwidth" title="AllocateBandwidth">AllocateBandwidth</a>" : <i>Double</i>,
        "<a href="#appliancename" title="ApplianceName">ApplianceName</a>" : <i>String</i>,
        "<a href="#burst" title="Burst">Burst</a>" : <i>Double</i>,
        "<a href="#enablerequests" title="EnableRequests">EnableRequests</a>" : <i>Double</i>,
        "<a href="#enterprise" title="Enterprise">Enterprise</a>" : <i>String</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#usemgmtport" title="UseMgmtPort">UseMgmtPort</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#proxyserver" title="ProxyServer">ProxyServer</a>" : <i>[ <a href="proxyserverdefinition.md">ProxyServerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::Glm
Properties:
    <a href="#allocatebandwidth" title="AllocateBandwidth">AllocateBandwidth</a>: <i>Double</i>
    <a href="#appliancename" title="ApplianceName">ApplianceName</a>: <i>String</i>
    <a href="#burst" title="Burst">Burst</a>: <i>Double</i>
    <a href="#enablerequests" title="EnableRequests">EnableRequests</a>: <i>Double</i>
    <a href="#enterprise" title="Enterprise">Enterprise</a>: <i>String</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#usemgmtport" title="UseMgmtPort">UseMgmtPort</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#proxyserver" title="ProxyServer">ProxyServer</a>: <i>
      - <a href="proxyserverdefinition.md">ProxyServerDefinition</a></i>
</pre>

## Properties

#### AllocateBandwidth

Enter the requested bandwidth in Mbps for Capacity Pool.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplianceName

Helpful identifier for this appliance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Burst

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRequests

Enable connection to the GLM.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enterprise

Enter the ELM hostname or IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Enter the desired ping interval in hours.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Proxy server port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

License entitlement token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMgmtPort

Use management port to connect to GLM.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyServer

_Required_: No

_Type_: List of <a href="proxyserverdefinition.md">ProxyServerDefinition</a>

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


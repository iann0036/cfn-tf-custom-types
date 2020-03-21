# Terraform::Linode::NodebalancerConfig

CloudFormation equivalent of linode_nodebalancer_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Linode::NodebalancerConfig",
    "Properties" : {
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#check" title="Check">Check</a>" : <i>String</i>,
        "<a href="#checkattempts" title="CheckAttempts">CheckAttempts</a>" : <i>Double</i>,
        "<a href="#checkbody" title="CheckBody">CheckBody</a>" : <i>String</i>,
        "<a href="#checkinterval" title="CheckInterval">CheckInterval</a>" : <i>Double</i>,
        "<a href="#checkpassive" title="CheckPassive">CheckPassive</a>" : <i>Boolean</i>,
        "<a href="#checkpath" title="CheckPath">CheckPath</a>" : <i>String</i>,
        "<a href="#checktimeout" title="CheckTimeout">CheckTimeout</a>" : <i>Double</i>,
        "<a href="#ciphersuite" title="CipherSuite">CipherSuite</a>" : <i>String</i>,
        "<a href="#nodebalancerid" title="NodebalancerId">NodebalancerId</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#sslcert" title="SslCert">SslCert</a>" : <i>String</i>,
        "<a href="#sslkey" title="SslKey">SslKey</a>" : <i>String</i>,
        "<a href="#stickiness" title="Stickiness">Stickiness</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Linode::NodebalancerConfig
Properties:
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#check" title="Check">Check</a>: <i>String</i>
    <a href="#checkattempts" title="CheckAttempts">CheckAttempts</a>: <i>Double</i>
    <a href="#checkbody" title="CheckBody">CheckBody</a>: <i>String</i>
    <a href="#checkinterval" title="CheckInterval">CheckInterval</a>: <i>Double</i>
    <a href="#checkpassive" title="CheckPassive">CheckPassive</a>: <i>Boolean</i>
    <a href="#checkpath" title="CheckPath">CheckPath</a>: <i>String</i>
    <a href="#checktimeout" title="CheckTimeout">CheckTimeout</a>: <i>Double</i>
    <a href="#ciphersuite" title="CipherSuite">CipherSuite</a>: <i>String</i>
    <a href="#nodebalancerid" title="NodebalancerId">NodebalancerId</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#sslcert" title="SslCert">SslCert</a>: <i>String</i>
    <a href="#sslkey" title="SslKey">SslKey</a>: <i>String</i>
    <a href="#stickiness" title="Stickiness">Stickiness</a>: <i>String</i>
</pre>

## Properties

#### Algorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Check

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckAttempts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckPassive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherSuite

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodebalancerId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stickiness

_Required_: No

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

#### NodeStatus

Returns the <code>NodeStatus</code> value.

#### SslCommonname

Returns the <code>SslCommonname</code> value.

#### SslFingerprint

Returns the <code>SslFingerprint</code> value.


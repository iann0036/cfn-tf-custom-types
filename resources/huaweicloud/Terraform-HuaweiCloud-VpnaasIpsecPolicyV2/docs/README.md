# Terraform::HuaweiCloud::VpnaasIpsecPolicyV2

Manages a V2 IPSec policy resource within HuaweiCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::VpnaasIpsecPolicyV2",
    "Properties" : {
        "<a href="#authalgorithm" title="AuthAlgorithm">AuthAlgorithm</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encapsulationmode" title="EncapsulationMode">EncapsulationMode</a>" : <i>String</i>,
        "<a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pfs" title="Pfs">Pfs</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#transformprotocol" title="TransformProtocol">TransformProtocol</a>" : <i>String</i>,
        "<a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>" : <i>[ <a href="valuespecs.md">ValueSpecs</a>, ... ]</i>,
        "<a href="#lifetime" title="Lifetime">Lifetime</a>" : <i>[ <a href="lifetime.md">Lifetime</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::VpnaasIpsecPolicyV2
Properties:
    <a href="#authalgorithm" title="AuthAlgorithm">AuthAlgorithm</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encapsulationmode" title="EncapsulationMode">EncapsulationMode</a>: <i>String</i>
    <a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pfs" title="Pfs">Pfs</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#transformprotocol" title="TransformProtocol">TransformProtocol</a>: <i>String</i>
    <a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>: <i>
      - <a href="valuespecs.md">ValueSpecs</a></i>
    <a href="#lifetime" title="Lifetime">Lifetime</a>: <i>
      - <a href="lifetime.md">Lifetime</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AuthAlgorithm

The authentication hash algorithm. Valid values are md5, sha1, sha2-256, sha2-384, sha2-512.
Default is sha1. Changing this updates the algorithm of the existing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The human-readable description for the policy.
Changing this updates the description of the existing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncapsulationMode

The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionAlgorithm

The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the policy. Changing this updates the name of
the existing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pfs

The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransformProtocol

The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSpecs

Map of additional options.

_Required_: No

_Type_: List of <a href="valuespecs.md">ValueSpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifetime

_Required_: No

_Type_: List of <a href="lifetime.md">Lifetime</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


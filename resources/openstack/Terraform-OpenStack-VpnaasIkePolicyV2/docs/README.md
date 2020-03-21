# Terraform::OpenStack::VpnaasIkePolicyV2

Manages a V2 Neutron IKE policy resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::VpnaasIkePolicyV2",
    "Properties" : {
        "<a href="#authalgorithm" title="AuthAlgorithm">AuthAlgorithm</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>" : <i>String</i>,
        "<a href="#ikeversion" title="IkeVersion">IkeVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pfs" title="Pfs">Pfs</a>" : <i>String</i>,
        "<a href="#phase1negotiationmode" title="Phase1NegotiationMode">Phase1NegotiationMode</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>" : <i>[ <a href="valuespecs.md">ValueSpecs</a>, ... ]</i>,
        "<a href="#lifetime" title="Lifetime">Lifetime</a>" : <i>[ <a href="lifetime.md">Lifetime</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::VpnaasIkePolicyV2
Properties:
    <a href="#authalgorithm" title="AuthAlgorithm">AuthAlgorithm</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>: <i>String</i>
    <a href="#ikeversion" title="IkeVersion">IkeVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pfs" title="Pfs">Pfs</a>: <i>String</i>
    <a href="#phase1negotiationmode" title="Phase1NegotiationMode">Phase1NegotiationMode</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>: <i>
      - <a href="valuespecs.md">ValueSpecs</a></i>
    <a href="#lifetime" title="Lifetime">Lifetime</a>: <i>
      - <a href="lifetime.md">Lifetime</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AuthAlgorithm

The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
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

#### EncryptionAlgorithm

The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeVersion

The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.

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

#### Phase1NegotiationMode

The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.

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


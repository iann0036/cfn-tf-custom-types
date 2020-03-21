# Terraform::Google::BinaryAuthorizationAttestor

CloudFormation equivalent of google_binary_authorization_attestor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::BinaryAuthorizationAttestor",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#attestationauthoritynote" title="AttestationAuthorityNote">AttestationAuthorityNote</a>" : <i>[ <a href="attestationauthoritynote.md">AttestationAuthorityNote</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#publickeys" title="PublicKeys">PublicKeys</a>" : <i>[ <a href="publickeys.md">PublicKeys</a>, ... ]</i>,
        "<a href="#pkixpublickey" title="PkixPublicKey">PkixPublicKey</a>" : <i>[ <a href="pkixpublickey.md">PkixPublicKey</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::BinaryAuthorizationAttestor
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#attestationauthoritynote" title="AttestationAuthorityNote">AttestationAuthorityNote</a>: <i>
      - <a href="attestationauthoritynote.md">AttestationAuthorityNote</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#publickeys" title="PublicKeys">PublicKeys</a>: <i>
      - <a href="publickeys.md">PublicKeys</a></i>
    <a href="#pkixpublickey" title="PkixPublicKey">PkixPublicKey</a>: <i>
      - <a href="pkixpublickey.md">PkixPublicKey</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttestationAuthorityNote

_Required_: No

_Type_: List of <a href="attestationauthoritynote.md">AttestationAuthorityNote</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeys

_Required_: No

_Type_: List of <a href="publickeys.md">PublicKeys</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PkixPublicKey

_Required_: No

_Type_: List of <a href="pkixpublickey.md">PkixPublicKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


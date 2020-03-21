# Terraform::AWS::KmsGrant

CloudFormation equivalent of aws_kms_grant

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::KmsGrant",
    "Properties" : {
        "<a href="#grantcreationtokens" title="GrantCreationTokens">GrantCreationTokens</a>" : <i>[ String, ... ]</i>,
        "<a href="#granteeprincipal" title="GranteePrincipal">GranteePrincipal</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#operations" title="Operations">Operations</a>" : <i>[ String, ... ]</i>,
        "<a href="#retireondelete" title="RetireOnDelete">RetireOnDelete</a>" : <i>Boolean</i>,
        "<a href="#retiringprincipal" title="RetiringPrincipal">RetiringPrincipal</a>" : <i>String</i>,
        "<a href="#constraints" title="Constraints">Constraints</a>" : <i>[ <a href="constraints.md">Constraints</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::KmsGrant
Properties:
    <a href="#grantcreationtokens" title="GrantCreationTokens">GrantCreationTokens</a>: <i>
      - String</i>
    <a href="#granteeprincipal" title="GranteePrincipal">GranteePrincipal</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#operations" title="Operations">Operations</a>: <i>
      - String</i>
    <a href="#retireondelete" title="RetireOnDelete">RetireOnDelete</a>: <i>Boolean</i>
    <a href="#retiringprincipal" title="RetiringPrincipal">RetiringPrincipal</a>: <i>String</i>
    <a href="#constraints" title="Constraints">Constraints</a>: <i>
      - <a href="constraints.md">Constraints</a></i>
</pre>

## Properties

#### GrantCreationTokens

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GranteePrincipal

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operations

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetireOnDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetiringPrincipal

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Constraints

_Required_: No

_Type_: List of <a href="constraints.md">Constraints</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### GrantId

Returns the <code>GrantId</code> value.

#### GrantToken

Returns the <code>GrantToken</code> value.


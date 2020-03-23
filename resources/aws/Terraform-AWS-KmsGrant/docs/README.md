# Terraform::AWS::KmsGrant

Provides a resource-based access control mechanism for a KMS customer master key.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::KmsGrant",
    "Properties" : {
        "<a href="#grantcreationtokens" title="GrantCreationTokens">GrantCreationTokens</a>" : <i>[ String, ... ]</i>,
        "<a href="#granteeprincipal" title="GranteePrincipal">GranteePrincipal</a>" : <i>String</i>,
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

A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GranteePrincipal

The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, terraform's state may not always be refreshed to reflect what is true in AWS.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A friendly name for identifying the grant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operations

A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetireOnDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetiringPrincipal

The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, terraform's state may not always be refreshed to reflect what is true in AWS.

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

#### Id

Returns the <code>Id</code> value.


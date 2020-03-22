# Terraform::OCI::IdentityUserCapabilitiesManagement

CloudFormation equivalent of oci_identity_user_capabilities_management

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::IdentityUserCapabilitiesManagement",
    "Properties" : {
        "<a href="#canuseapikeys" title="CanUseApiKeys">CanUseApiKeys</a>" : <i>Boolean</i>,
        "<a href="#canuseauthtokens" title="CanUseAuthTokens">CanUseAuthTokens</a>" : <i>Boolean</i>,
        "<a href="#canuseconsolepassword" title="CanUseConsolePassword">CanUseConsolePassword</a>" : <i>Boolean</i>,
        "<a href="#canusecustomersecretkeys" title="CanUseCustomerSecretKeys">CanUseCustomerSecretKeys</a>" : <i>Boolean</i>,
        "<a href="#canusesmtpcredentials" title="CanUseSmtpCredentials">CanUseSmtpCredentials</a>" : <i>Boolean</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::IdentityUserCapabilitiesManagement
Properties:
    <a href="#canuseapikeys" title="CanUseApiKeys">CanUseApiKeys</a>: <i>Boolean</i>
    <a href="#canuseauthtokens" title="CanUseAuthTokens">CanUseAuthTokens</a>: <i>Boolean</i>
    <a href="#canuseconsolepassword" title="CanUseConsolePassword">CanUseConsolePassword</a>: <i>Boolean</i>
    <a href="#canusecustomersecretkeys" title="CanUseCustomerSecretKeys">CanUseCustomerSecretKeys</a>: <i>Boolean</i>
    <a href="#canusesmtpcredentials" title="CanUseSmtpCredentials">CanUseSmtpCredentials</a>: <i>Boolean</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CanUseApiKeys

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanUseAuthTokens

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanUseConsolePassword

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanUseCustomerSecretKeys

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanUseSmtpCredentials

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


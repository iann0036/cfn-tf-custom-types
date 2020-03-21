# Terraform::AzureRM::VpnServerConfiguration AzureActiveDirectoryAuthentication

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#audience" title="Audience">Audience</a>" : <i>String</i>,
    "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
    "<a href="#tenant" title="Tenant">Tenant</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#audience" title="Audience">Audience</a>: <i>String</i>
<a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
<a href="#tenant" title="Tenant">Tenant</a>: <i>String</i>
</pre>

## Properties

#### Audience

The Audience which should be used for authentication.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

The Issuer which should be used for authentication.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenant

The Tenant which should be used for authentication.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


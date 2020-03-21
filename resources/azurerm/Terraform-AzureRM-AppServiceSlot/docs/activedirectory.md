# Terraform::AzureRM::AppServiceSlot ActiveDirectory

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedaudiences" title="AllowedAudiences">AllowedAudiences</a>" : <i>[ String, ... ]</i>,
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowedaudiences" title="AllowedAudiences">AllowedAudiences</a>: <i>
      - String</i>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
</pre>

## Properties

#### AllowedAudiences

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


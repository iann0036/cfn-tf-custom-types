# Terraform::AzureAD::Application AppRole

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedmembertypes" title="AllowedMemberTypes">AllowedMemberTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowedmembertypes" title="AllowedMemberTypes">AllowedMemberTypes</a>: <i>
      - String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### AllowedMemberTypes

Specifies whether this app role definition can be assigned to users and groups by setting to `User`, or to other applications (that are accessing this application in daemon service scenarios) by setting to `Application`, or to both.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Permission help text that appears in the admin app assignment and consent experiences.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name for the permission that appears in the admin consent and app assignment experiences.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

Determines if the app role is enabled: Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

Specifies the value of the roles claim that the application should expect in the authentication and access tokens.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# TF::Nutanix::User IdentityProviderUserDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#identityproviderreference" title="IdentityProviderReference">IdentityProviderReference</a>" : <i>[ <a href="identityproviderreferencedefinition.md">IdentityProviderReferenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#identityproviderreference" title="IdentityProviderReference">IdentityProviderReference</a>: <i>
      - <a href="identityproviderreferencedefinition.md">IdentityProviderReferenceDefinition</a></i>
</pre>

## Properties

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityProviderReference

_Required_: No

_Type_: List of <a href="identityproviderreferencedefinition.md">IdentityProviderReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


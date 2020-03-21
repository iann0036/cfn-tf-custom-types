# Terraform::AWS::CognitoIdentityPoolRolesAttachment RoleMapping

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ambiguousroleresolution" title="AmbiguousRoleResolution">AmbiguousRoleResolution</a>" : <i>String</i>,
    "<a href="#identityprovider" title="IdentityProvider">IdentityProvider</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#mappingrule" title="MappingRule">MappingRule</a>" : <i>[ <a href="rolemapping-mappingrule.md">MappingRule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ambiguousroleresolution" title="AmbiguousRoleResolution">AmbiguousRoleResolution</a>: <i>String</i>
<a href="#identityprovider" title="IdentityProvider">IdentityProvider</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#mappingrule" title="MappingRule">MappingRule</a>: <i>
      - <a href="rolemapping-mappingrule.md">MappingRule</a></i>
</pre>

## Properties

#### AmbiguousRoleResolution

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityProvider

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappingRule

_Required_: No
_Type_: List of <a href="rolemapping-mappingrule.md">MappingRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


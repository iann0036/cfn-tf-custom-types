# Terraform::AWS::CognitoIdentityPoolRolesAttachment RoleMapping

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ambiguousroleresolution" title="AmbiguousRoleResolution">AmbiguousRoleResolution</a>" : <i>String</i>,
    "<a href="#identityprovider" title="IdentityProvider">IdentityProvider</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#mappingrule" title="MappingRule">MappingRule</a>" : <i>[ &lt;a href=&#34;rolemapping-mappingrule.md&#34;&gt;MappingRule&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ambiguousroleresolution" title="AmbiguousRoleResolution">AmbiguousRoleResolution</a>: <i>String</i>
<a href="#identityprovider" title="IdentityProvider">IdentityProvider</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#mappingrule" title="MappingRule">MappingRule</a>: <i>
      - &lt;a href=&#34;rolemapping-mappingrule.md&#34;&gt;MappingRule&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;rolemapping-mappingrule.md&#34;&gt;MappingRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


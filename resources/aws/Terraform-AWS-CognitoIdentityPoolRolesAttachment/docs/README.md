# Terraform::AWS::CognitoIdentityPoolRolesAttachment

CloudFormation equivalent of aws_cognito_identity_pool_roles_attachment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CognitoIdentityPoolRolesAttachment",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#identitypoolid" title="IdentityPoolId">IdentityPoolId</a>" : <i>String</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ &lt;a href=&#34;roles.md&#34;&gt;Roles&lt;/a&gt;, ... ]</i>,
        "<a href="#rolemapping" title="RoleMapping">RoleMapping</a>" : <i>[ &lt;a href=&#34;rolemapping.md&#34;&gt;RoleMapping&lt;/a&gt;, ... ]</i>,
        "<a href="#mappingrule" title="MappingRule">MappingRule</a>" : <i>[ &lt;a href=&#34;mappingrule.md&#34;&gt;MappingRule&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CognitoIdentityPoolRolesAttachment
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#identitypoolid" title="IdentityPoolId">IdentityPoolId</a>: <i>String</i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - &lt;a href=&#34;roles.md&#34;&gt;Roles&lt;/a&gt;</i>
    <a href="#rolemapping" title="RoleMapping">RoleMapping</a>: <i>
      - &lt;a href=&#34;rolemapping.md&#34;&gt;RoleMapping&lt;/a&gt;</i>
    <a href="#mappingrule" title="MappingRule">MappingRule</a>: <i>
      - &lt;a href=&#34;mappingrule.md&#34;&gt;MappingRule&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityPoolId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: Yes

_Type_: List of &lt;a href=&#34;roles.md&#34;&gt;Roles&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleMapping

_Required_: No

_Type_: List of &lt;a href=&#34;rolemapping.md&#34;&gt;RoleMapping&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappingRule

_Required_: No

_Type_: List of &lt;a href=&#34;mappingrule.md&#34;&gt;MappingRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


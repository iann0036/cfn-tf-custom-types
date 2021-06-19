# TF::Gitlab::GroupVariable

This resource allows you to create and manage CI/CD variables for your GitLab groups.
For further information on variables, consult the [gitlab
documentation](https://docs.gitlab.com/ce/ci/variables/README.html#variables).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::GroupVariable",
    "Properties" : {
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#masked" title="Masked">Masked</a>" : <i>Boolean</i>,
        "<a href="#protected" title="Protected">Protected</a>" : <i>Boolean</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
        "<a href="#variabletype" title="VariableType">VariableType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::GroupVariable
Properties:
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#masked" title="Masked">Masked</a>: <i>Boolean</i>
    <a href="#protected" title="Protected">Protected</a>: <i>Boolean</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
    <a href="#variabletype" title="VariableType">VariableType</a>: <i>String</i>
</pre>

## Properties

#### Group

The name or id of the group to add the hook to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The name of the variable.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Masked

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protected

If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value of the variable.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VariableType

The type of a variable. Available types are: env_var (default) and file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


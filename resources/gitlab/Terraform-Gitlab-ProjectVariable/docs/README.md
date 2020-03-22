# Terraform::Gitlab::ProjectVariable

This resource allows you to create and manage CI/CD variables for your GitLab projects.
For further information on variables, consult the [gitlab
documentation](https://docs.gitlab.com/ce/ci/variables/README.html#variables).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::ProjectVariable",
    "Properties" : {
        "<a href="#environmentscope" title="EnvironmentScope">EnvironmentScope</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#masked" title="Masked">Masked</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#protected" title="Protected">Protected</a>" : <i>Boolean</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
        "<a href="#variabletype" title="VariableType">VariableType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Gitlab::ProjectVariable
Properties:
    <a href="#environmentscope" title="EnvironmentScope">EnvironmentScope</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#masked" title="Masked">Masked</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#protected" title="Protected">Protected</a>: <i>Boolean</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
    <a href="#variabletype" title="VariableType">VariableType</a>: <i>String</i>
</pre>

## Properties

#### EnvironmentScope

The environment_scope of the variable.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The name of the variable.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Masked

If set to `true`, the variable will be masked if it would have been written to the logs. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or id of the project to add the hook to.

_Required_: Yes

_Type_: String

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


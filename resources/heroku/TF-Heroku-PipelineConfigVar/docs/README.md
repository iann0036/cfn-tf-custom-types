# TF::Heroku::PipelineConfigVar

Provides a resource to manage a pipeline's config vars.

The pipeline config var API can only retrieve config vars that can be set at the pipeline level.
Additionally, these two supported pipeline stages are:
- [Heroku CI](https://devcenter.heroku.com/articles/heroku-ci#setting-environment-variables-the-env-key) config vars (test stage)
- [Review Apps](https://devcenter.heroku.com/articles/github-integration-review-apps#configuration) config vars (review stage)

The development, staging & production stages do not have stage-level config vars, only those on the apps within each stage.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Heroku::PipelineConfigVar",
    "Properties" : {
        "<a href="#pipelineid" title="PipelineId">PipelineId</a>" : <i>String</i>,
        "<a href="#pipelinestage" title="PipelineStage">PipelineStage</a>" : <i>String</i>,
        "<a href="#sensitivevars" title="SensitiveVars">SensitiveVars</a>" : <i>[ <a href="sensitivevarsdefinition.md">SensitiveVarsDefinition</a>, ... ]</i>,
        "<a href="#vars" title="Vars">Vars</a>" : <i>[ <a href="varsdefinition.md">VarsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Heroku::PipelineConfigVar
Properties:
    <a href="#pipelineid" title="PipelineId">PipelineId</a>: <i>String</i>
    <a href="#pipelinestage" title="PipelineStage">PipelineStage</a>: <i>String</i>
    <a href="#sensitivevars" title="SensitiveVars">SensitiveVars</a>: <i>
      - <a href="sensitivevarsdefinition.md">SensitiveVarsDefinition</a></i>
    <a href="#vars" title="Vars">Vars</a>: <i>
      - <a href="varsdefinition.md">VarsDefinition</a></i>
</pre>

## Properties

#### PipelineId

The UUID of an existing pipeline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineStage

The pipeline's stage. Supported values are `test` & `review`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensitiveVars

This is the same as `vars`. The main difference between the two attributes is `sensitive_vars` outputs
are redacted on-screen and replaced by a `<sensitive>` placeholder, following a terraform `plan` or `apply`.
It is recommended to put private keys, passwords, etc in this argument.

_Required_: No

_Type_: List of <a href="sensitivevarsdefinition.md">SensitiveVarsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

Map of config vars that can be output in plaintext.

_Required_: No

_Type_: List of <a href="varsdefinition.md">VarsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllVars

Returns the <code>AllVars</code> value.

#### Id

Returns the <code>Id</code> value.


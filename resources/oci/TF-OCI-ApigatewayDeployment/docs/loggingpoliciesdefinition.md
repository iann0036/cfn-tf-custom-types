# TF::OCI::ApigatewayDeployment LoggingPoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesslog" title="AccessLog">AccessLog</a>" : <i>[ <a href="accesslogdefinition.md">AccessLogDefinition</a>, ... ]</i>,
    "<a href="#executionlog" title="ExecutionLog">ExecutionLog</a>" : <i>[ <a href="executionlogdefinition.md">ExecutionLogDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesslog" title="AccessLog">AccessLog</a>: <i>
      - <a href="accesslogdefinition.md">AccessLogDefinition</a></i>
<a href="#executionlog" title="ExecutionLog">ExecutionLog</a>: <i>
      - <a href="executionlogdefinition.md">ExecutionLogDefinition</a></i>
</pre>

## Properties

#### AccessLog

_Required_: No

_Type_: List of <a href="accesslogdefinition.md">AccessLogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionLog

_Required_: No

_Type_: List of <a href="executionlogdefinition.md">ExecutionLogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


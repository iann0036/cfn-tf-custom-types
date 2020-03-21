# Terraform::Datadog::LogsPipelineOrder

Provides a Datadog [Logs Pipeline API](https://docs.datadoghq.com/api/?lang=python#logs-pipelines) resource, which is used to manage Datadog log pipelines order.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::LogsPipelineOrder",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pipelines" title="Pipelines">Pipelines</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::LogsPipelineOrder
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pipelines" title="Pipelines">Pipelines</a>: <i>
      - String</i>
</pre>

## Properties

#### Name

The name attribute in the resource `datadog_logs_pipeline_order` needs to be unique. It's recommended to use the same value as the resource `NAME`.
No related field is available in  [Logs Pipeline API](https://docs.datadoghq.com/api/?lang=python#get-pipeline-order).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pipelines

The pipeline IDs list. The order of pipeline IDs in this attribute defines the overall pipeline order for logs.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


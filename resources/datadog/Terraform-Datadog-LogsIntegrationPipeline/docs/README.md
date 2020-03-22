# Terraform::Datadog::LogsIntegrationPipeline

Provides a Datadog [Logs Pipeline API](https://docs.datadoghq.com/api/?lang=python#logs-pipelines) resource to manage
the [integrations](https://docs.datadoghq.com/logs/log_collection/?tab=tcpussite).

Integration pipelines are the pipelines that are automatically installed for your organization when sending the logs with 
specific sources. You don't need to maintain or update these types of pipelines. Keeping them as resources, however, 
allows you to manage the order of your pipelines by referencing them in your 
[datadog_logs_pipeline_order](logs_pipeline_order.html#datadog_logs_pipeline_order) resource. If you don't need the
`pipeline_order` feature, this resource declaration can be omitted.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::LogsIntegrationPipeline",
    "Properties" : {
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::LogsIntegrationPipeline
Properties:
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### IsEnabled

Boolean value to enable your pipeline.

_Required_: No

_Type_: Boolean

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


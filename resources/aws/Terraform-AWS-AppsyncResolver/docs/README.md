# Terraform::AWS::AppsyncResolver

Provides an AppSync Resolver.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AppsyncResolver",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#datasource" title="DataSource">DataSource</a>" : <i>String</i>,
        "<a href="#field" title="Field">Field</a>" : <i>String</i>,
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#requesttemplate" title="RequestTemplate">RequestTemplate</a>" : <i>String</i>,
        "<a href="#responsetemplate" title="ResponseTemplate">ResponseTemplate</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#pipelineconfig" title="PipelineConfig">PipelineConfig</a>" : <i>[ <a href="pipelineconfig.md">PipelineConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AppsyncResolver
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#datasource" title="DataSource">DataSource</a>: <i>String</i>
    <a href="#field" title="Field">Field</a>: <i>String</i>
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#requesttemplate" title="RequestTemplate">RequestTemplate</a>: <i>String</i>
    <a href="#responsetemplate" title="ResponseTemplate">ResponseTemplate</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#pipelineconfig" title="PipelineConfig">PipelineConfig</a>: <i>
      - <a href="pipelineconfig.md">PipelineConfig</a></i>
</pre>

## Properties

#### ApiId

The API ID for the GraphQL API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSource

The DataSource name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

The field name from the schema defined in the GraphQL API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

The resolver type. Valid values are `UNIT` and `PIPELINE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTemplate

The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTemplate

The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type name from the schema defined in the GraphQL API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineConfig

_Required_: No

_Type_: List of <a href="pipelineconfig.md">PipelineConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.


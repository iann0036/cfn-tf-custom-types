# Terraform::AWS::AppsyncDatasource

CloudFormation equivalent of aws_appsync_datasource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AppsyncDatasource",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#dynamodbconfig" title="DynamodbConfig">DynamodbConfig</a>" : <i>[ &lt;a href=&#34;dynamodbconfig.md&#34;&gt;DynamodbConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#elasticsearchconfig" title="ElasticsearchConfig">ElasticsearchConfig</a>" : <i>[ &lt;a href=&#34;elasticsearchconfig.md&#34;&gt;ElasticsearchConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#httpconfig" title="HttpConfig">HttpConfig</a>" : <i>[ &lt;a href=&#34;httpconfig.md&#34;&gt;HttpConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>" : <i>[ &lt;a href=&#34;lambdaconfig.md&#34;&gt;LambdaConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AppsyncDatasource
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#dynamodbconfig" title="DynamodbConfig">DynamodbConfig</a>: <i>
      - &lt;a href=&#34;dynamodbconfig.md&#34;&gt;DynamodbConfig&lt;/a&gt;</i>
    <a href="#elasticsearchconfig" title="ElasticsearchConfig">ElasticsearchConfig</a>: <i>
      - &lt;a href=&#34;elasticsearchconfig.md&#34;&gt;ElasticsearchConfig&lt;/a&gt;</i>
    <a href="#httpconfig" title="HttpConfig">HttpConfig</a>: <i>
      - &lt;a href=&#34;httpconfig.md&#34;&gt;HttpConfig&lt;/a&gt;</i>
    <a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>: <i>
      - &lt;a href=&#34;lambdaconfig.md&#34;&gt;LambdaConfig&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamodbConfig

_Required_: No

_Type_: List of &lt;a href=&#34;dynamodbconfig.md&#34;&gt;DynamodbConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchConfig

_Required_: No

_Type_: List of &lt;a href=&#34;elasticsearchconfig.md&#34;&gt;ElasticsearchConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpConfig

_Required_: No

_Type_: List of &lt;a href=&#34;httpconfig.md&#34;&gt;HttpConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaConfig

_Required_: No

_Type_: List of &lt;a href=&#34;lambdaconfig.md&#34;&gt;LambdaConfig&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.


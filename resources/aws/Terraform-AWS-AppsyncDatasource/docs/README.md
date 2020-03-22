# Terraform::AWS::AppsyncDatasource

CloudFormation equivalent of aws_appsync_datasource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AppsyncDatasource",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#dynamodbconfig" title="DynamodbConfig">DynamodbConfig</a>" : <i>[ <a href="dynamodbconfig.md">DynamodbConfig</a>, ... ]</i>,
        "<a href="#elasticsearchconfig" title="ElasticsearchConfig">ElasticsearchConfig</a>" : <i>[ <a href="elasticsearchconfig.md">ElasticsearchConfig</a>, ... ]</i>,
        "<a href="#httpconfig" title="HttpConfig">HttpConfig</a>" : <i>[ <a href="httpconfig.md">HttpConfig</a>, ... ]</i>,
        "<a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>" : <i>[ <a href="lambdaconfig.md">LambdaConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AppsyncDatasource
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#dynamodbconfig" title="DynamodbConfig">DynamodbConfig</a>: <i>
      - <a href="dynamodbconfig.md">DynamodbConfig</a></i>
    <a href="#elasticsearchconfig" title="ElasticsearchConfig">ElasticsearchConfig</a>: <i>
      - <a href="elasticsearchconfig.md">ElasticsearchConfig</a></i>
    <a href="#httpconfig" title="HttpConfig">HttpConfig</a>: <i>
      - <a href="httpconfig.md">HttpConfig</a></i>
    <a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>: <i>
      - <a href="lambdaconfig.md">LambdaConfig</a></i>
</pre>

## Properties

#### ApiId

_Required_: Yes

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

_Type_: List of <a href="dynamodbconfig.md">DynamodbConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchConfig

_Required_: No

_Type_: List of <a href="elasticsearchconfig.md">ElasticsearchConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpConfig

_Required_: No

_Type_: List of <a href="httpconfig.md">HttpConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaConfig

_Required_: No

_Type_: List of <a href="lambdaconfig.md">LambdaConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.


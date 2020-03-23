# Terraform::AWS::CodepipelineWebhook

Provides a CodePipeline Webhook.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodepipelineWebhook",
    "Properties" : {
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#targetaction" title="TargetAction">TargetAction</a>" : <i>String</i>,
        "<a href="#targetpipeline" title="TargetPipeline">TargetPipeline</a>" : <i>String</i>,
        "<a href="#authenticationconfiguration" title="AuthenticationConfiguration">AuthenticationConfiguration</a>" : <i>[ <a href="authenticationconfiguration.md">AuthenticationConfiguration</a>, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filter.md">Filter</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodepipelineWebhook
Properties:
    <a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#targetaction" title="TargetAction">TargetAction</a>: <i>String</i>
    <a href="#targetpipeline" title="TargetPipeline">TargetPipeline</a>: <i>String</i>
    <a href="#authenticationconfiguration" title="AuthenticationConfiguration">AuthenticationConfiguration</a>: <i>
      - <a href="authenticationconfiguration.md">AuthenticationConfiguration</a></i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filter.md">Filter</a></i>
</pre>

## Properties

#### Authentication

The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the webhook.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAction

The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPipeline

The name of the pipeline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationConfiguration

_Required_: No

_Type_: List of <a href="authenticationconfiguration.md">AuthenticationConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filter.md">Filter</a>

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

#### Url

Returns the <code>Url</code> value.


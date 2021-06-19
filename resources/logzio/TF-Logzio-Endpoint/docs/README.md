# TF::Logzio::Endpoint

CloudFormation equivalent of logzio_endpoint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Logzio::Endpoint",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#endpointtype" title="EndpointType">EndpointType</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#bigpanda" title="BigPanda">BigPanda</a>" : <i>[ <a href="bigpandadefinition.md">BigPandaDefinition</a>, ... ]</i>,
        "<a href="#custom" title="Custom">Custom</a>" : <i>[ <a href="customdefinition.md">CustomDefinition</a>, ... ]</i>,
        "<a href="#datadog" title="DataDog">DataDog</a>" : <i>[ <a href="datadogdefinition.md">DataDogDefinition</a>, ... ]</i>,
        "<a href="#pagerduty" title="PagerDuty">PagerDuty</a>" : <i>[ <a href="pagerdutydefinition.md">PagerDutyDefinition</a>, ... ]</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>,
        "<a href="#victorops" title="Victorops">Victorops</a>" : <i>[ <a href="victoropsdefinition.md">VictoropsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Logzio::Endpoint
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#endpointtype" title="EndpointType">EndpointType</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#bigpanda" title="BigPanda">BigPanda</a>: <i>
      - <a href="bigpandadefinition.md">BigPandaDefinition</a></i>
    <a href="#custom" title="Custom">Custom</a>: <i>
      - <a href="customdefinition.md">CustomDefinition</a></i>
    <a href="#datadog" title="DataDog">DataDog</a>: <i>
      - <a href="datadogdefinition.md">DataDogDefinition</a></i>
    <a href="#pagerduty" title="PagerDuty">PagerDuty</a>: <i>
      - <a href="pagerdutydefinition.md">PagerDutyDefinition</a></i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
    <a href="#victorops" title="Victorops">Victorops</a>: <i>
      - <a href="victoropsdefinition.md">VictoropsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigPanda

_Required_: No

_Type_: List of <a href="bigpandadefinition.md">BigPandaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Custom

_Required_: No

_Type_: List of <a href="customdefinition.md">CustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDog

_Required_: No

_Type_: List of <a href="datadogdefinition.md">DataDogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PagerDuty

_Required_: No

_Type_: List of <a href="pagerdutydefinition.md">PagerDutyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slackdefinition.md">SlackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Victorops

_Required_: No

_Type_: List of <a href="victoropsdefinition.md">VictoropsDefinition</a>

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


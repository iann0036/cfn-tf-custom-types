# Terraform::AWS::LbListener DefaultAction FixedResponse

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
    "<a href="#messagebody" title="MessageBody">MessageBody</a>" : <i>String</i>,
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
<a href="#messagebody" title="MessageBody">MessageBody</a>: <i>String</i>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
</pre>

## Properties

#### ContentType

The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageBody

The message body.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


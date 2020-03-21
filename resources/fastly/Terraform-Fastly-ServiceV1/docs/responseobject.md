# Terraform::Fastly::ServiceV1 ResponseObject

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cachecondition" title="CacheCondition">CacheCondition</a>" : <i>String</i>,
    "<a href="#content" title="Content">Content</a>" : <i>String</i>,
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#requestcondition" title="RequestCondition">RequestCondition</a>" : <i>String</i>,
    "<a href="#response" title="Response">Response</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#cachecondition" title="CacheCondition">CacheCondition</a>: <i>String</i>
<a href="#content" title="Content">Content</a>: <i>String</i>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#requestcondition" title="RequestCondition">RequestCondition</a>: <i>String</i>
<a href="#response" title="Response">Response</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>Double</i>
</pre>

## Properties

#### CacheCondition

Name of already defined `condition` to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This `condition` must be of type `CACHE`. For detailed information about Conditionals,
see [Fastly's Documentation on Conditionals][fastly-conditionals].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

The content to deliver for the response object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

The MIME type of the content.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify this Response Object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestCondition

Name of already defined `condition` to be checked during the request phase. If the condition passes then this object will be delivered. This `condition` must be of type `REQUEST`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Response

The HTTP Response. Default `Ok`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The HTTP Status Code. Default `200`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


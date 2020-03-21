# Terraform::Fastly::ServiceV1 Gzip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cachecondition" title="CacheCondition">CacheCondition</a>" : <i>String</i>,
    "<a href="#contenttypes" title="ContentTypes">ContentTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#extensions" title="Extensions">Extensions</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cachecondition" title="CacheCondition">CacheCondition</a>: <i>String</i>
<a href="#contenttypes" title="ContentTypes">ContentTypes</a>: <i>
      - String</i>
<a href="#extensions" title="Extensions">Extensions</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### CacheCondition

Name of already defined `condition` to apply. This `condition` must be of type `CACHE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentTypes

The content-type for each type of content you wish to
have dynamically gzip'ed. Example: `["text/html", "text/css"]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extensions

File extensions for each file type to dynamically
gzip. Example: `["css", "js"]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Unique name for this header attribute.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


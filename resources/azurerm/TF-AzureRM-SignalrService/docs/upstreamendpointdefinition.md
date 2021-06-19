# TF::AzureRM::SignalrService UpstreamEndpointDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#categorypattern" title="CategoryPattern">CategoryPattern</a>" : <i>[ String, ... ]</i>,
    "<a href="#eventpattern" title="EventPattern">EventPattern</a>" : <i>[ String, ... ]</i>,
    "<a href="#hubpattern" title="HubPattern">HubPattern</a>" : <i>[ String, ... ]</i>,
    "<a href="#urltemplate" title="UrlTemplate">UrlTemplate</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#categorypattern" title="CategoryPattern">CategoryPattern</a>: <i>
      - String</i>
<a href="#eventpattern" title="EventPattern">EventPattern</a>: <i>
      - String</i>
<a href="#hubpattern" title="HubPattern">HubPattern</a>: <i>
      - String</i>
<a href="#urltemplate" title="UrlTemplate">UrlTemplate</a>: <i>String</i>
</pre>

## Properties

#### CategoryPattern

The categories to match on, or `*` for all.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventPattern

The events to match on, or `*` for all.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HubPattern

The hubs to match on, or `*` for all.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlTemplate

The upstream URL Template. This can be a url or a template such as `http://host.com/{hub}/api/{category}/{event}`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


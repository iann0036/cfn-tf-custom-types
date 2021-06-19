# TF::Google::ContainerCluster ReleaseChannelDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#channel" title="Channel">Channel</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#channel" title="Channel">Channel</a>: <i>String</i>
</pre>

## Properties

#### Channel

The selected release channel.
Accepted values are:
* UNSPECIFIED: Not set.
* RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.
* REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.
* STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# Terraform::ACME::Certificate DnsChallenge

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#config" title="Config">Config</a>" : <i>[ <a href="dnschallenge-config.md">Config</a>, ... ]</i>,
    "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#config" title="Config">Config</a>: <i>
      - <a href="dnschallenge-config.md">Config</a></i>
<a href="#provider" title="Provider">Provider</a>: <i>String</i>
</pre>

## Properties

#### Config

_Required_: No
_Type_: List of <a href="dnschallenge-config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


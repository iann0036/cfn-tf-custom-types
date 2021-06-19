# TF::AzureRM::MssqlElasticpool PerDatabaseSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>" : <i>Double</i>,
    "<a href="#mincapacity" title="MinCapacity">MinCapacity</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>: <i>Double</i>
<a href="#mincapacity" title="MinCapacity">MinCapacity</a>: <i>Double</i>
</pre>

## Properties

#### MaxCapacity

The maximum capacity any one database can consume.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCapacity

The minimum capacity all databases are guaranteed.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# TF::AWS::EmrCluster InstanceTypeConfigsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bidprice" title="BidPrice">BidPrice</a>" : <i>String</i>,
    "<a href="#bidpriceaspercentageofondemandprice" title="BidPriceAsPercentageOfOnDemandPrice">BidPriceAsPercentageOfOnDemandPrice</a>" : <i>Double</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#weightedcapacity" title="WeightedCapacity">WeightedCapacity</a>" : <i>Double</i>,
    "<a href="#configurations" title="Configurations">Configurations</a>" : <i>[ <a href="configurationsdefinition.md">ConfigurationsDefinition</a>, ... ]</i>,
    "<a href="#ebsconfig" title="EbsConfig">EbsConfig</a>" : <i>[ <a href="ebsconfigdefinition.md">EbsConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bidprice" title="BidPrice">BidPrice</a>: <i>String</i>
<a href="#bidpriceaspercentageofondemandprice" title="BidPriceAsPercentageOfOnDemandPrice">BidPriceAsPercentageOfOnDemandPrice</a>: <i>Double</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#weightedcapacity" title="WeightedCapacity">WeightedCapacity</a>: <i>Double</i>
<a href="#configurations" title="Configurations">Configurations</a>: <i>
      - <a href="configurationsdefinition.md">ConfigurationsDefinition</a></i>
<a href="#ebsconfig" title="EbsConfig">EbsConfig</a>: <i>
      - <a href="ebsconfigdefinition.md">EbsConfigDefinition</a></i>
</pre>

## Properties

#### BidPrice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BidPriceAsPercentageOfOnDemandPrice

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configurations

_Required_: No

_Type_: List of <a href="configurationsdefinition.md">ConfigurationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsConfig

_Required_: No

_Type_: List of <a href="ebsconfigdefinition.md">EbsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


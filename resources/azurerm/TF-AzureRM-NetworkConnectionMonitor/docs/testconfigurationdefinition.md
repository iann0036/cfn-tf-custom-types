# TF::AzureRM::NetworkConnectionMonitor TestConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#preferredipversion" title="PreferredIpVersion">PreferredIpVersion</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#testfrequencyinseconds" title="TestFrequencyInSeconds">TestFrequencyInSeconds</a>" : <i>Double</i>,
    "<a href="#httpconfiguration" title="HttpConfiguration">HttpConfiguration</a>" : <i>[ <a href="httpconfigurationdefinition.md">HttpConfigurationDefinition</a>, ... ]</i>,
    "<a href="#icmpconfiguration" title="IcmpConfiguration">IcmpConfiguration</a>" : <i>[ <a href="icmpconfigurationdefinition.md">IcmpConfigurationDefinition</a>, ... ]</i>,
    "<a href="#successthreshold" title="SuccessThreshold">SuccessThreshold</a>" : <i>[ <a href="successthresholddefinition.md">SuccessThresholdDefinition</a>, ... ]</i>,
    "<a href="#tcpconfiguration" title="TcpConfiguration">TcpConfiguration</a>" : <i>[ <a href="tcpconfigurationdefinition.md">TcpConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#preferredipversion" title="PreferredIpVersion">PreferredIpVersion</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#testfrequencyinseconds" title="TestFrequencyInSeconds">TestFrequencyInSeconds</a>: <i>Double</i>
<a href="#httpconfiguration" title="HttpConfiguration">HttpConfiguration</a>: <i>
      - <a href="httpconfigurationdefinition.md">HttpConfigurationDefinition</a></i>
<a href="#icmpconfiguration" title="IcmpConfiguration">IcmpConfiguration</a>: <i>
      - <a href="icmpconfigurationdefinition.md">IcmpConfigurationDefinition</a></i>
<a href="#successthreshold" title="SuccessThreshold">SuccessThreshold</a>: <i>
      - <a href="successthresholddefinition.md">SuccessThresholdDefinition</a></i>
<a href="#tcpconfiguration" title="TcpConfiguration">TcpConfiguration</a>: <i>
      - <a href="tcpconfigurationdefinition.md">TcpConfigurationDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredIpVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestFrequencyInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpConfiguration

_Required_: No

_Type_: List of <a href="httpconfigurationdefinition.md">HttpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpConfiguration

_Required_: No

_Type_: List of <a href="icmpconfigurationdefinition.md">IcmpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessThreshold

_Required_: No

_Type_: List of <a href="successthresholddefinition.md">SuccessThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpConfiguration

_Required_: No

_Type_: List of <a href="tcpconfigurationdefinition.md">TcpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# TF::Dynatrace::Autotag MetadataDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
    "<a href="#configurationversions" title="ConfigurationVersions">ConfigurationVersions</a>" : <i>[ Double, ... ]</i>,
    "<a href="#currentconfigurationversions" title="CurrentConfigurationVersions">CurrentConfigurationVersions</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
<a href="#configurationversions" title="ConfigurationVersions">ConfigurationVersions</a>: <i>
      - Double</i>
<a href="#currentconfigurationversions" title="CurrentConfigurationVersions">CurrentConfigurationVersions</a>: <i>
      - String</i>
</pre>

## Properties

#### ClusterVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationVersions

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CurrentConfigurationVersions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


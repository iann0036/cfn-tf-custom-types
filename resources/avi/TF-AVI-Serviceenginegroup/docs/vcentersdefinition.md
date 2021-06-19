# TF::AVI::Serviceenginegroup VcentersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#vcenterfolder" title="VcenterFolder">VcenterFolder</a>" : <i>String</i>,
    "<a href="#vcenterref" title="VcenterRef">VcenterRef</a>" : <i>String</i>,
    "<a href="#nsxtclusters" title="NsxtClusters">NsxtClusters</a>" : <i>[ <a href="nsxtclustersdefinition.md">NsxtClustersDefinition</a>, ... ]</i>,
    "<a href="#nsxtdatastores" title="NsxtDatastores">NsxtDatastores</a>" : <i>[ <a href="nsxtdatastoresdefinition.md">NsxtDatastoresDefinition</a>, ... ]</i>,
    "<a href="#nsxthosts" title="NsxtHosts">NsxtHosts</a>" : <i>[ <a href="nsxthostsdefinition.md">NsxtHostsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#vcenterfolder" title="VcenterFolder">VcenterFolder</a>: <i>String</i>
<a href="#vcenterref" title="VcenterRef">VcenterRef</a>: <i>String</i>
<a href="#nsxtclusters" title="NsxtClusters">NsxtClusters</a>: <i>
      - <a href="nsxtclustersdefinition.md">NsxtClustersDefinition</a></i>
<a href="#nsxtdatastores" title="NsxtDatastores">NsxtDatastores</a>: <i>
      - <a href="nsxtdatastoresdefinition.md">NsxtDatastoresDefinition</a></i>
<a href="#nsxthosts" title="NsxtHosts">NsxtHosts</a>: <i>
      - <a href="nsxthostsdefinition.md">NsxtHostsDefinition</a></i>
</pre>

## Properties

#### VcenterFolder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterRef

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtClusters

_Required_: No

_Type_: List of <a href="nsxtclustersdefinition.md">NsxtClustersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtDatastores

_Required_: No

_Type_: List of <a href="nsxtdatastoresdefinition.md">NsxtDatastoresDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtHosts

_Required_: No

_Type_: List of <a href="nsxthostsdefinition.md">NsxtHostsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


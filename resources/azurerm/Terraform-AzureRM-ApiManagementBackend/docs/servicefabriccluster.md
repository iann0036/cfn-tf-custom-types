# Terraform::AzureRM::ApiManagementBackend ServiceFabricCluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientcertificatethumbprint" title="ClientCertificateThumbprint">ClientCertificateThumbprint</a>" : <i>String</i>,
    "<a href="#managementendpoints" title="ManagementEndpoints">ManagementEndpoints</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxpartitionresolutionretries" title="MaxPartitionResolutionRetries">MaxPartitionResolutionRetries</a>" : <i>Double</i>,
    "<a href="#servercertificatethumbprints" title="ServerCertificateThumbprints">ServerCertificateThumbprints</a>" : <i>[ String, ... ]</i>,
    "<a href="#serverx509name" title="ServerX509Name">ServerX509Name</a>" : <i>[ &lt;a href=&#34;servicefabriccluster-serverx509name.md&#34;&gt;ServerX509Name&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientcertificatethumbprint" title="ClientCertificateThumbprint">ClientCertificateThumbprint</a>: <i>String</i>
<a href="#managementendpoints" title="ManagementEndpoints">ManagementEndpoints</a>: <i>
      - String</i>
<a href="#maxpartitionresolutionretries" title="MaxPartitionResolutionRetries">MaxPartitionResolutionRetries</a>: <i>Double</i>
<a href="#servercertificatethumbprints" title="ServerCertificateThumbprints">ServerCertificateThumbprints</a>: <i>
      - String</i>
<a href="#serverx509name" title="ServerX509Name">ServerX509Name</a>: <i>
      - &lt;a href=&#34;servicefabriccluster-serverx509name.md&#34;&gt;ServerX509Name&lt;/a&gt;</i>
</pre>

## Properties

#### ClientCertificateThumbprint

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementEndpoints

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPartitionResolutionRetries

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateThumbprints

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerX509Name

_Required_: No
_Type_: List of &lt;a href=&#34;servicefabriccluster-serverx509name.md&#34;&gt;ServerX509Name&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


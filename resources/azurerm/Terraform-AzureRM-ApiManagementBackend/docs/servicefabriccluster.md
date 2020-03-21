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
    "<a href="#serverx509name" title="ServerX509Name">ServerX509Name</a>" : <i>[ <a href="servicefabriccluster-serverx509name.md">ServerX509Name</a>, ... ]</i>
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
      - <a href="servicefabriccluster-serverx509name.md">ServerX509Name</a></i>
</pre>

## Properties

#### ClientCertificateThumbprint

The client certificate thumbprint for the management endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementEndpoints

A list of cluster management endpoints.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPartitionResolutionRetries

The maximum number of retries when attempting resolve the partition.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateThumbprints

A list of thumbprints of the server certificates of the Service Fabric cluster.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerX509Name

_Required_: No

_Type_: List of <a href="servicefabriccluster-serverx509name.md">ServerX509Name</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# Terraform::Google::ComposerEnvironment

An environment for running orchestration tasks.

Environments run Apache Airflow software on Google infrastructure.

To get more information about Environments, see:

* [API documentation](https://cloud.google.com/composer/docs/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/composer/docs)
    * [Configuring Shared VPC for Composer Environments](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc)
* [Apache Airflow Documentation](http://airflow.apache.org/)

~> **Warning:** We **STRONGLY** recommend  you read the [GCP guides](https://cloud.google.com/composer/docs/how-to)
  as the Environment resource requires a long deployment process and involves several layers of GCP infrastructure, 
  including a Kubernetes Engine cluster, Cloud Storage, and Compute networking resources. Due to limitations of the API,
  Terraform will not be able to automatically find or manage many of these underlying resources. In particular:
  * It can take up to one hour to create or update an environment resource. In addition, GCP may only detect some 
    errors in configuration when they are used (e.g. ~40-50 minutes into the creation process), and is prone to limited
    error reporting. If you encounter confusing or uninformative errors, please verify your configuration is valid 
    against GCP Cloud Composer before filing bugs against the Terraform provider. 
  * **Environments create Google Cloud Storage buckets that do not get cleaned up automatically** on environment 
    deletion. [More about Composer's use of Cloud Storage](https://cloud.google.com/composer/docs/concepts/cloud-storage).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComposerEnvironment",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="config.md">Config</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfig.md">NodeConfig</a>, ... ]</i>,
        "<a href="#privateenvironmentconfig" title="PrivateEnvironmentConfig">PrivateEnvironmentConfig</a>" : <i>[ <a href="privateenvironmentconfig.md">PrivateEnvironmentConfig</a>, ... ]</i>,
        "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ <a href="softwareconfig.md">SoftwareConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComposerEnvironment
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="config.md">Config</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfig.md">NodeConfig</a></i>
    <a href="#privateenvironmentconfig" title="PrivateEnvironmentConfig">PrivateEnvironmentConfig</a>: <i>
      - <a href="privateenvironmentconfig.md">PrivateEnvironmentConfig</a></i>
    <a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - <a href="softwareconfig.md">SoftwareConfig</a></i>
</pre>

## Properties

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No

_Type_: List of <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfig.md">NodeConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEnvironmentConfig

_Required_: No

_Type_: List of <a href="privateenvironmentconfig.md">PrivateEnvironmentConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No

_Type_: List of <a href="softwareconfig.md">SoftwareConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


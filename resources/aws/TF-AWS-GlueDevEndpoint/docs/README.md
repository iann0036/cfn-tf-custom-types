# TF::AWS::GlueDevEndpoint

Provides a Glue Development Endpoint resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::GlueDevEndpoint",
    "Properties" : {
        "<a href="#arguments" title="Arguments">Arguments</a>" : <i>[ <a href="argumentsdefinition.md">ArgumentsDefinition</a>, ... ]</i>,
        "<a href="#extrajarss3path" title="ExtraJarsS3Path">ExtraJarsS3Path</a>" : <i>String</i>,
        "<a href="#extrapythonlibss3path" title="ExtraPythonLibsS3Path">ExtraPythonLibsS3Path</a>" : <i>String</i>,
        "<a href="#glueversion" title="GlueVersion">GlueVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numberofnodes" title="NumberOfNodes">NumberOfNodes</a>" : <i>Double</i>,
        "<a href="#numberofworkers" title="NumberOfWorkers">NumberOfWorkers</a>" : <i>Double</i>,
        "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>,
        "<a href="#publickeys" title="PublicKeys">PublicKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#workertype" title="WorkerType">WorkerType</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::GlueDevEndpoint
Properties:
    <a href="#arguments" title="Arguments">Arguments</a>: <i>
      - <a href="argumentsdefinition.md">ArgumentsDefinition</a></i>
    <a href="#extrajarss3path" title="ExtraJarsS3Path">ExtraJarsS3Path</a>: <i>String</i>
    <a href="#extrapythonlibss3path" title="ExtraPythonLibsS3Path">ExtraPythonLibsS3Path</a>: <i>String</i>
    <a href="#glueversion" title="GlueVersion">GlueVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numberofnodes" title="NumberOfNodes">NumberOfNodes</a>: <i>Double</i>
    <a href="#numberofworkers" title="NumberOfWorkers">NumberOfWorkers</a>: <i>Double</i>
    <a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
    <a href="#publickeys" title="PublicKeys">PublicKeys</a>: <i>
      - String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#workertype" title="WorkerType">WorkerType</a>: <i>String</i>
</pre>

## Properties

#### Arguments

A map of arguments used to configure the endpoint.

_Required_: No

_Type_: List of <a href="argumentsdefinition.md">ArgumentsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraJarsS3Path

Path to one or more Java Jars in an S3 bucket that should be loaded in this endpoint.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraPythonLibsS3Path

Path(s) to one or more Python libraries in an S3 bucket that should be loaded in this endpoint. Multiple values must be complete paths separated by a comma.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlueVersion

-  Specifies the versions of Python and Apache Spark to use. Defaults to AWS Glue version 0.9.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of this endpoint. It must be unique in your account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfNodes

The number of AWS Glue Data Processing Units (DPUs) to allocate to this endpoint. Conflicts with `worker_type`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfWorkers

The number of workers of a defined worker type that are allocated to this endpoint. This field is available only when you choose worker type G.1X or G.2X.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKey

The public key to be used by this endpoint for authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeys

A list of public keys to be used by this endpoint for authentication.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The IAM role for this endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfiguration

The name of the Security Configuration structure to be used with this endpoint.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

Security group IDs for the security groups to be used by this endpoint.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The subnet ID for the new endpoint to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerType

The type of predefined worker that is allocated to this endpoint. Accepts a value of Standard, G.1X, or G.2X.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### AvailabilityZone

Returns the <code>AvailabilityZone</code> value.

#### FailureReason

Returns the <code>FailureReason</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrivateAddress

Returns the <code>PrivateAddress</code> value.

#### PublicAddress

Returns the <code>PublicAddress</code> value.

#### Status

Returns the <code>Status</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

#### YarnEndpointAddress

Returns the <code>YarnEndpointAddress</code> value.

#### ZeppelinRemoteSparkInterpreterPort

Returns the <code>ZeppelinRemoteSparkInterpreterPort</code> value.


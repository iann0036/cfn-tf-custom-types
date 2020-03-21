# Terraform::Panos::PanoramaLogForwardingProfile

CloudFormation equivalent of panos_panorama_log_forwarding_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaLogForwardingProfile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#enhancedlogging" title="EnhancedLogging">EnhancedLogging</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#matchlist" title="MatchList">MatchList</a>" : <i>[ <a href="matchlist.md">MatchList</a>, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ <a href="action.md">Action</a>, ... ]</i>,
        "<a href="#azureintegration" title="AzureIntegration">AzureIntegration</a>" : <i>[ <a href="azureintegration.md">AzureIntegration</a>, ... ]</i>,
        "<a href="#taggingintegration" title="TaggingIntegration">TaggingIntegration</a>" : <i>[ <a href="taggingintegration.md">TaggingIntegration</a>, ... ]</i>,
        "<a href="#localregistration" title="LocalRegistration">LocalRegistration</a>" : <i>[ <a href="localregistration.md">LocalRegistration</a>, ... ]</i>,
        "<a href="#panoramaregistration" title="PanoramaRegistration">PanoramaRegistration</a>" : <i>[ <a href="panoramaregistration.md">PanoramaRegistration</a>, ... ]</i>,
        "<a href="#remoteregistration" title="RemoteRegistration">RemoteRegistration</a>" : <i>[ <a href="remoteregistration.md">RemoteRegistration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaLogForwardingProfile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#enhancedlogging" title="EnhancedLogging">EnhancedLogging</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#matchlist" title="MatchList">MatchList</a>: <i>
      - <a href="matchlist.md">MatchList</a></i>
    <a href="#action" title="Action">Action</a>: <i>
      - <a href="action.md">Action</a></i>
    <a href="#azureintegration" title="AzureIntegration">AzureIntegration</a>: <i>
      - <a href="azureintegration.md">AzureIntegration</a></i>
    <a href="#taggingintegration" title="TaggingIntegration">TaggingIntegration</a>: <i>
      - <a href="taggingintegration.md">TaggingIntegration</a></i>
    <a href="#localregistration" title="LocalRegistration">LocalRegistration</a>: <i>
      - <a href="localregistration.md">LocalRegistration</a></i>
    <a href="#panoramaregistration" title="PanoramaRegistration">PanoramaRegistration</a>: <i>
      - <a href="panoramaregistration.md">PanoramaRegistration</a></i>
    <a href="#remoteregistration" title="RemoteRegistration">RemoteRegistration</a>: <i>
      - <a href="remoteregistration.md">RemoteRegistration</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedLogging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchList

_Required_: No

_Type_: List of <a href="matchlist.md">MatchList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="action.md">Action</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureIntegration

_Required_: No

_Type_: List of <a href="azureintegration.md">AzureIntegration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaggingIntegration

_Required_: No

_Type_: List of <a href="taggingintegration.md">TaggingIntegration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalRegistration

_Required_: No

_Type_: List of <a href="localregistration.md">LocalRegistration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanoramaRegistration

_Required_: No

_Type_: List of <a href="panoramaregistration.md">PanoramaRegistration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteRegistration

_Required_: No

_Type_: List of <a href="remoteregistration.md">RemoteRegistration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


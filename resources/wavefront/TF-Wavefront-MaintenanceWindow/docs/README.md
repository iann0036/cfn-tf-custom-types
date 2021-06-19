# TF::Wavefront::MaintenanceWindow

CloudFormation equivalent of wavefront_maintenance_window

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::MaintenanceWindow",
    "Properties" : {
        "<a href="#endtimeinseconds" title="EndTimeInSeconds">EndTimeInSeconds</a>" : <i>Double</i>,
        "<a href="#hosttaggrouphostnamesgroupanded" title="HostTagGroupHostNamesGroupAnded">HostTagGroupHostNamesGroupAnded</a>" : <i>Boolean</i>,
        "<a href="#reason" title="Reason">Reason</a>" : <i>String</i>,
        "<a href="#relevantcustomertags" title="RelevantCustomerTags">RelevantCustomerTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#relevanthostnames" title="RelevantHostNames">RelevantHostNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#relevanthosttags" title="RelevantHostTags">RelevantHostTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#relevanthosttagsanded" title="RelevantHostTagsAnded">RelevantHostTagsAnded</a>" : <i>Boolean</i>,
        "<a href="#starttimeinseconds" title="StartTimeInSeconds">StartTimeInSeconds</a>" : <i>Double</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::MaintenanceWindow
Properties:
    <a href="#endtimeinseconds" title="EndTimeInSeconds">EndTimeInSeconds</a>: <i>Double</i>
    <a href="#hosttaggrouphostnamesgroupanded" title="HostTagGroupHostNamesGroupAnded">HostTagGroupHostNamesGroupAnded</a>: <i>Boolean</i>
    <a href="#reason" title="Reason">Reason</a>: <i>String</i>
    <a href="#relevantcustomertags" title="RelevantCustomerTags">RelevantCustomerTags</a>: <i>
      - String</i>
    <a href="#relevanthostnames" title="RelevantHostNames">RelevantHostNames</a>: <i>
      - String</i>
    <a href="#relevanthosttags" title="RelevantHostTags">RelevantHostTags</a>: <i>
      - String</i>
    <a href="#relevanthosttagsanded" title="RelevantHostTagsAnded">RelevantHostTagsAnded</a>: <i>Boolean</i>
    <a href="#starttimeinseconds" title="StartTimeInSeconds">StartTimeInSeconds</a>: <i>Double</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### EndTimeInSeconds

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostTagGroupHostNamesGroupAnded

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reason

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelevantCustomerTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelevantHostNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelevantHostTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelevantHostTagsAnded

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTimeInSeconds

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.


# TF::SignalFx::Detector

Provides a SignalFx detector resource. This can be used to create and manage detectors.

~> **NOTE** If you're interested in using SignalFx detector features such as Historical Anomaly, Resource Running Out, or others then consider building them in the UI first then using the "Show SignalFlow" feature to extract the value for `program_text`. You may also consult the [documentation for detector functions in signalflow-library](https://github.com/signalfx/signalflow-library/tree/master/library/signalfx/detectors).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::Detector",
    "Properties" : {
        "<a href="#authorizedwriterteams" title="AuthorizedWriterTeams">AuthorizedWriterTeams</a>" : <i>[ String, ... ]</i>,
        "<a href="#authorizedwriterusers" title="AuthorizedWriterUsers">AuthorizedWriterUsers</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disablesampling" title="DisableSampling">DisableSampling</a>" : <i>Boolean</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>Double</i>,
        "<a href="#maxdelay" title="MaxDelay">MaxDelay</a>" : <i>Double</i>,
        "<a href="#mindelay" title="MinDelay">MinDelay</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#programtext" title="ProgramText">ProgramText</a>" : <i>String</i>,
        "<a href="#showdatamarkers" title="ShowDataMarkers">ShowDataMarkers</a>" : <i>Boolean</i>,
        "<a href="#showeventlines" title="ShowEventLines">ShowEventLines</a>" : <i>Boolean</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#teams" title="Teams">Teams</a>" : <i>[ String, ... ]</i>,
        "<a href="#timerange" title="TimeRange">TimeRange</a>" : <i>Double</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>,
        "<a href="#vizoptions" title="VizOptions">VizOptions</a>" : <i>[ <a href="vizoptionsdefinition.md">VizOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::Detector
Properties:
    <a href="#authorizedwriterteams" title="AuthorizedWriterTeams">AuthorizedWriterTeams</a>: <i>
      - String</i>
    <a href="#authorizedwriterusers" title="AuthorizedWriterUsers">AuthorizedWriterUsers</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disablesampling" title="DisableSampling">DisableSampling</a>: <i>Boolean</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>Double</i>
    <a href="#maxdelay" title="MaxDelay">MaxDelay</a>: <i>Double</i>
    <a href="#mindelay" title="MinDelay">MinDelay</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#programtext" title="ProgramText">ProgramText</a>: <i>String</i>
    <a href="#showdatamarkers" title="ShowDataMarkers">ShowDataMarkers</a>: <i>Boolean</i>
    <a href="#showeventlines" title="ShowEventLines">ShowEventLines</a>: <i>Boolean</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#teams" title="Teams">Teams</a>: <i>
      - String</i>
    <a href="#timerange" title="TimeRange">TimeRange</a>: <i>Double</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
    <a href="#vizoptions" title="VizOptions">VizOptions</a>: <i>
      - <a href="vizoptionsdefinition.md">VizOptionsDefinition</a></i>
</pre>

## Properties

#### AuthorizedWriterTeams

Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedWriterUsers

User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
* `disabled` - (Optional) When true, notifications and events will not be generated for the detect label. `false` by default.
* `notifications` - (Optional) List of strings specifying where notifications will be sent when an incident occurs. See [Create A Single Detector](https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector) for more info.
* `parameterized_body` - (Optional) Custom notification message body when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
* `parameterized_subject` - (Optional) Custom notification message subject when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
* `runbook_url` - (Optional) URL of page to consult when an alert is triggered. This can be used with custom notification messages.
* `tip` - (Optional) Plain text suggested first course of action, such as a command line to execute. This can be used with custom notification messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSampling

When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

Seconds since epoch. Used for visualization. Conflicts with `time_range`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDelay

How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinDelay

How long (in seconds) to wait even if the datapoints are arriving in a timely fashion. Max value is 900 (15m).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the detector.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProgramText

Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowDataMarkers

When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowEventLines

When `true`, the visualization will display a vertical line for each event trigger. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Seconds since epoch. Used for visualization. Conflicts with `time_range`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags associated with the detector.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

Team IDs to associate the detector to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRange

Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VizOptions

_Required_: No

_Type_: List of <a href="vizoptionsdefinition.md">VizOptionsDefinition</a>

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

#### Url

Returns the <code>Url</code> value.

